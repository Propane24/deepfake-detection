function scanMedia() {
  const images = document.querySelectorAll("img");
  const videos = document.querySelectorAll("video");

  images.forEach(img => {
    const dummyScore = Math.random(); // Replace with real model score later
    addOverlay(img, dummyScore);
  });

  videos.forEach(video => {
    const dummyScore = Math.random();
    addOverlay(video, dummyScore);
  });
}

function addOverlay(element, score) {
  // Remove old overlays if re-scanning
  const existing = element.parentElement.querySelector(".auth-overlay");
  if (existing) existing.remove();

  const percentage = (score * 100).toFixed(1);

  // Determine color
  let color;
  if (percentage >= 60) {
    color = "green";
  } else if (percentage >= 40) {
    color = "orange";
  } else {
    color = "red";
  }

  // Create container
  const overlay = document.createElement("div");
  overlay.className = "auth-overlay";

  overlay.style.position = "absolute";
  overlay.style.top = "-28px";
  overlay.style.left = "0";
  overlay.style.display = "flex";
  overlay.style.alignItems = "center";
  overlay.style.gap = "6px";
  overlay.style.padding = "4px 8px";
  overlay.style.background = "rgba(0,0,0,0.75)";
  overlay.style.color = "white";
  overlay.style.fontSize = "12px";
  overlay.style.fontWeight = "bold";
  overlay.style.borderRadius = "6px";
  overlay.style.zIndex = "9999";

  // Create colored light
  const light = document.createElement("div");
  light.style.width = "10px";
  light.style.height = "10px";
  light.style.borderRadius = "50%";
  light.style.backgroundColor = color;

  // Add score text
  const text = document.createElement("span");
  text.innerText = percentage + "% Authentic";

  overlay.appendChild(light);
  overlay.appendChild(text);

  // Ensure parent is positioned
  element.parentElement.style.position = "relative";

  element.parentElement.appendChild(overlay);
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "scanMedia") {
    scanMedia();
  }
});