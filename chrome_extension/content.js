chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'extractText') {
        // Extract visible text from the page
        const pageText = document.body.innerText.trim();
        sendResponse({ text: pageText });
    }
});
