(() => {
  const url = new URL(window.location.href);
  if (url.hostname !== "github.com") {
    return;
  }
  url.hostname = "devinreview.com";

  const button = document.createElement("a");
  button.id = "devin-review-button";
  button.href = url.toString();
  button.target = "_blank";
  button.rel = "noopener noreferrer";
  button.textContent = "Open in Devin Review";
  document.body.appendChild(button);
})();
