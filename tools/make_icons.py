#!/usr/bin/env python3
"""Generate PNG icons for the extension (blue rounded square + white play glyph).

Pure stdlib: supersamples 4x and box-downsamples, writes PNG via zlib.
Usage: python3 tools/make_icons.py
"""
import os
import struct
import zlib

SS = 4  # supersample factor
BG = (47, 111, 219, 255)  # #2f6fdb
FG = (255, 255, 255, 255)
RADIUS = 0.22
# Right-pointing triangle in unit coords.
TRI = [(0.36, 0.27), (0.36, 0.73), (0.70, 0.50)]


def in_rounded_rect(x, y):
    r = RADIUS
    cx = min(max(x, r), 1 - r)
    cy = min(max(y, r), 1 - r)
    return (x - cx) ** 2 + (y - cy) ** 2 <= r * r


def in_tri(x, y):
    (x1, y1), (x2, y2), (x3, y3) = TRI
    d = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / d
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / d
    c = 1 - a - b
    return a >= 0 and b >= 0 and c >= 0


def render(size):
    n = size * SS
    acc = [[[0] * 4 for _ in range(size)] for _ in range(size)]
    for sy in range(n):
        for sx in range(n):
            x, y = (sx + 0.5) / n, (sy + 0.5) / n
            px = int(sx / SS)
            py = int(sy / SS)
            color = FG if in_tri(x, y) else BG if in_rounded_rect(x, y) else (0, 0, 0, 0)
            for i in range(4):
                acc[py][px][i] += color[i]
    px_count = SS * SS
    rows = b""
    for y in range(size):
        rows += b"\x00"
        for x in range(size):
            rows += bytes(c // px_count for c in acc[y][x])
    return rows


def chunk(tag, data):
    return (
        struct.pack(">I", len(data))
        + tag
        + data
        + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    )


def write_png(path, size):
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(render(size), 9))
        + chunk(b"IEND", b"")
    )
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(png)


if __name__ == "__main__":
    for sub in ("firefox", "chrome"):
        for size in (16, 48, 128):
            write_png(f"{sub}/icons/icon-{size}.png", size)
            print(f"{sub}/icons/icon-{size}.png")
