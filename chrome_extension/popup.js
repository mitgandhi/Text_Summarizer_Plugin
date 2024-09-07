document.getElementById('summarize-btn').addEventListener('click', summarizePage);
document.getElementById('clear-cache-btn').addEventListener('click', clearCache);

async function summarizePage() {
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const response = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: getPageText
    });

    const pageText = response[0].result;

    if (pageText) {
      document.getElementById('summary').innerText = 'Summarizing...';
      const summaryResponse = await fetch('http://127.0.0.1:5000/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: pageText }),
      });

      if (!summaryResponse.ok) {
        throw new Error(`HTTP error! status: ${summaryResponse.status}`);
      }

      const summaryData = await summaryResponse.json();
      if (summaryData.error) {
        throw new Error(summaryData.error);
      }
      document.getElementById('summary').innerText = summaryData.summary_text || 'Error summarizing text.';
    } else {
      document.getElementById('summary').innerText = 'No text found on this page.';
    }
  } catch (error) {
    console.error('Error in summarizePage:', error);
    document.getElementById('summary').innerText = `Error summarizing text: ${error.message}`;
  }
}

function getPageText() {
  return document.body.innerText || '';
}

async function clearCache() {
  try {
    await chrome.runtime.sendMessage({ action: 'clearCache' });
    document.getElementById('summary').innerText = 'Cache cleared successfully.';
  } catch (error) {
    console.error('Error in clearCache:', error);
    document.getElementById('summary').innerText = `Error clearing cache: ${error.message}`;
  }
}

// Open the popup in a separate window to prevent it from closing
chrome.action.onClicked.addListener((tab) => {
  chrome.windows.create({
    url: 'popup.html',
    type: 'popup',
    width: 400,
    height: 600
  });
});