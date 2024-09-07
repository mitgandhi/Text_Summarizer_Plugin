# Page Summarizer Chrome Extension

This Chrome extension allows you to summarize the content of any webpage with a single click. It uses a Python backend with a machine learning model to generate concise summaries.

## Prerequisites

Before you begin, ensure you have the following installed on your Windows computer:

1. Google Chrome browser
2. Visual Studio Code (VS Code)
3. Python (version 3.7 or higher)
4. Git (optional, but recommended)

If you don't have these installed, follow these steps:

1. Download and install Google Chrome from [here](https://www.google.com/chrome/).
2. Download and install Visual Studio Code from [here](https://code.visualstudio.com/download).
3. Download and install Python from [here](https://www.python.org/downloads/). During installation, make sure to check the box that says "Add Python to PATH".
4. (Optional) Download and install Git from [here](https://git-scm.com/download/win).

## Setting Up the Project

1. Create a new folder on your computer where you want to store the project.

2. Open Visual Studio Code.

3. In VS Code, go to File > Open Folder and select the folder you just created.

4. Open a new terminal in VS Code by going to Terminal > New Terminal.

5. In the terminal, run the following commands one by one:

   ```
   git clone https://github.com/your-username/page-summarizer.git
   cd page-summarizer
   ```

   If you don't have Git, you can download the project as a ZIP file and extract it into your folder.

6. Create a virtual environment by running:

   ```
   python -m venv venv
   ```

7. Activate the virtual environment:

   ```
   venv\Scripts\activate
   ```

8. Install the required Python packages:

   ```
   pip install flask flask-cors transformers torch
   ```

## Running the Backend Server

1. In the VS Code terminal, make sure you're in the project directory and the virtual environment is activated.

2. Start the Flask server by running:

   ```
   python app.py
   ```

3. You should see a message saying the server is running on http://127.0.0.1:5000/.

4. Keep this terminal window open while using the extension.

## Installing the Chrome Extension

1. Open Google Chrome.

2. Type `chrome://extensions/` in the address bar and press Enter.

3. Enable "Developer mode" by toggling the switch in the top right corner.

4. Click on "Load unpacked" in the top left corner.

5. Navigate to your project folder and select the folder containing the extension files (manifest.json, popup.html, etc.).

6. The Page Summarizer extension should now appear in your list of extensions.

## Using the Extension

1. Make sure the Flask server is running (step 3 in "Running the Backend Server").

2. Click on the Page Summarizer extension icon in Chrome.

3. In the popup window, click "Summarize Page".

4. Wait a few moments for the summary to appear.

5. To clear the cache, click the "Clear Cache" button.

## Troubleshooting

If you encounter any issues:

1. Make sure the Flask server is running.
2. Check if you've installed all required Python packages.
3. Ensure you're using the correct Python version (3.7 or higher).
4. Try reloading the extension in Chrome.
5. Check the console in Chrome DevTools for any error messages.

If problems persist, please open an issue on the GitHub repository.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
