from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import re
import os
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG)

try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    logging.info("Summarization model loaded successfully")
except Exception as e:
    logging.error(f"Error loading summarization model: {str(e)}")
    summarizer = None

def clean_text(text):
    text = re.sub(r'[\r\n]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_text(text, max_length=1024):
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        logging.warning("No text provided")
        return jsonify({'error': 'No text provided'}), 400

    cleaned_text = clean_text(text)

    file_path = os.path.join(os.path.dirname(__file__), 'summarization_output.txt')
    logging.info(f'File path for output: {file_path}')

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f'Collected Text:\n{text}\n\n')
            f.write(f'Cleaned Text:\n{cleaned_text}\n\n')

            if len(cleaned_text) < 50:
                f.write('Error: Text is too short to summarize\n')
                logging.warning("Text is too short to summarize")
                return jsonify({'error': 'Text is too short to summarize'}), 400

            chunks = split_text(cleaned_text)
            summaries = []

            for chunk in chunks:
                f.write(f'Summarizing Chunk:\n{chunk}\n')
                if summarizer is None:
                    raise Exception("Summarization model not loaded")
                summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
                summary_text = summary[0]['summary_text']
                summaries.append(summary_text)
                f.write(f'Summary:\n{summary_text}\n')

            full_summary = " ".join(summaries)
            f.write(f'\nFull Summary:\n{full_summary}\n')
            logging.info(f'Successfully wrote to file: {file_path}')
            return jsonify({'summary_text': full_summary})
    except Exception as e:
        logging.error(f"Error during summarization: {str(e)}")
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f'Error during summarization: {e}\n')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)