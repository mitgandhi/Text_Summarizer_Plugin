chrome.runtime.onInstalled.addListener(() => {
  console.log("Text Summarizer Extension Installed");
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'clearCache') {
    clearCache();
    sendResponse({ message: 'Cache cleared' });
  }
});

function clearCache() {
  // Clear the browser cache
  chrome.browsingData.removeCache({}, () => {
    console.log('Browser cache cleared');
  });

  // Clear the extension's local storage
  chrome.storage.local.clear(() => {
    console.log('Extension local storage cleared');
  });
}