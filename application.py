from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from helpers.openai_helper import gpt3_completion
from helpers.pdf_helper import read_pdf
from helpers.text_helper import split_text

application = Flask(__name__)
load_dotenv()

@application.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@application.route('/summarize', methods=['POST'])
def summarize():
  if 'file' not in request.files:
    return jsonify({'error': 'No file part'})

  file = request.files['file']

  if file.filename == '':
    return jsonify({'error': 'No selected file'})
  
  pdf_text = read_pdf(file)
  
  chunks = split_text(pdf_text)
  
  summaries = []
  for chunk in chunks:
    prompt = 'Please summarize the following document: \n'
    summary = gpt3_completion(prompt + chunk)

    if summary.startswith('GPT-3 error:'):
      continue

    summaries.append(summary)
  
  summarized_text = ''.join(summaries)

  return jsonify({'summary': summarized_text})

if __name__ == '__main__':
  application.run(debug=True)
