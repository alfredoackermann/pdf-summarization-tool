# PDF Summarization Tool

This project implements a PDF summarization tool using Python, Flask, and the OpenAI API. The tool extracts content from uploaded PDF files, sends it to the OpenAI API for text summarization, and displays the summarized text to the user. The frontend provides an easy-to-use interface for users to interact with the tool.

## Demo

You can try out the PDF Summarization Tool by visiting the demo link:

**Demo Link:** [PDF Summarization Tool Demo](http://pdf-summarization-tool.us-east-2.elasticbeanstalk.com/)

Please note that this demo link may not be available indefinitely and is provided for testing purposes.

## Prerequisites

1. **Python:** Make sure you have Python 3.x installed on your system.

2. **OpenAI API Key:** You need an API key from OpenAI to use their services. If you don't have one, sign up on the OpenAI website and obtain your API key.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/alfredoackermann/pdf-summarization-tool.git
   cd pdf-summarization-tool
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**

   Create a `.env` file in the project directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your-openai-api-key
   ```

## Running the Application

1. **Run the Flask App:**

   ```bash
   python app.py
   ```

   This will start the Flask development server.

2. **Access the Application:**

   Open your web browser and go to `http://127.0.0.1:5000` to access the PDF summarization tool.

3. **Usage:**

   - Click the "Choose File" button to upload a PDF document.
   - Click the "Summarize" button to generate a summary of the PDF content.
   - The summarized text will be displayed on the page.

## Approach

### Backend Implementation

The backend of the application is developed using Flask, a lightweight web framework. The main steps of the backend implementation are as follows:

1. **API Endpoint**: Created an API endpoint that accepts a PDF file upload.
2. **PDF Content Extraction**: Used the PyMuPDF library to extract text content from the uploaded PDF.
3. **OpenAI Integration**: Sent the extracted text to the OpenAI API for text summarization using the `text-davinci-003` engine.
4. **Response Generation**: Processed the OpenAI API response to extract the summarized text.
5. **API Response**: Returned the summarized text as a JSON response.

### OpenAI API Integration

The OpenAI API is integrated into the backend to perform text summarization. The API key is stored as an environment variable and accessed using the `openai` Python library. The extracted text from the PDF is sent to the OpenAI API using the `Completion.create` method, and the response contains the summarized text.

### Preprocessing PDF Content

In the process of preparing PDF content for summarization, it's important to handle the potentially lengthy and complex text found within these documents. One challenge is dealing with long paragraphs that might contain multiple ideas or pieces of information. To address this, the `nltk.tokenize.sent_tokenize` function from the Natural Language Toolkit (NLTK) library is employed to segment the text into sentences, making it more manageable for summarization.

#### Sentence Tokenization

Sentence tokenization involves breaking down a paragraph or a larger block of text into individual sentences. This step is crucial as it helps in preserving the context of the original content while allowing the summarization model to work on shorter chunks of text. By applying sentence tokenization to the extracted text from the PDF, each sentence becomes a separate unit for summarization. This allows the summarization model to generate concise summaries that capture the main ideas of each individual sentence.Once the text has been tokenized into sentences, each sentence can be sent to the OpenAI API for summarization. This approach ensures that the summarization process is focused on smaller portions of text, which can lead to more coherent and contextually accurate summaries.

## Use Cases

The PDF summarization tool has several potential use cases, including:

- **Research and Study**: Students and researchers can quickly extract key information from lengthy research papers, articles, and reports.
- **Document Review**: Professionals can efficiently review contracts, legal documents, and reports by obtaining concise summaries.
- **Content Curation**: Content creators can extract the main points from multiple articles to curate content for their audience.

## Frontend

The frontend provides a user-friendly interface for users to interact with the PDF summarization tool. The frontend is implemented using HTML, CSS, and JavaScript:

- **File Upload**: Users can upload a PDF file using the file input element.
- **Summarize Button**: The "Summarize" button triggers the summarization process and displays the result.
- **Summarized Text Display**: The summarized text is displayed in a designated area.

Design choices for the frontend include a clean and responsive layout using CSS for styling and JavaScript to handle user interactions. The frontend communicates with the backend API using fetch requests to send PDF files and receive summarized text.
