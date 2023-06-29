chrome.runtime.onMessage.addListener((obj, sender, response) => {
  const { type, value, videoId } = obj;

  if (type === "NEW") {
    console.log("NEW VIDEO LOADED: " + videoId);
  }
});
