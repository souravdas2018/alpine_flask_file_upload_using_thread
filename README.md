# 📄 Flask Document Upload & AI Assistant

A Flask web application that enables users to upload PDF and Word documents, extracts their text content, and provides an AI-powered assistant to answer questions about the uploaded documents using OpenAI's GPT models.

## ✨ Features

- **Multi-File Upload**: Upload multiple PDF, DOC, and DOCX files simultaneously
- **Real-Time Progress Tracking**: Visual progress indicators with status updates
- **Threaded Processing**: Asynchronous file processing using Python threading
- **Text Extraction**: Automatic text extraction from PDF and Word documents
- **AI-Powered Q&A**: Ask questions about your documents using OpenAI GPT-4o-mini
- **Interactive UI**: Modern, responsive interface built with Alpine.js
- **Duplicate Detection**: Prevents uploading the same file twice
- **Animated Responses**: Word-by-word animated display of AI responses

## 🛠️ Technologies Used

### Backend
- **Flask** - Python web framework
- **OpenAI API** - GPT-4o-mini for intelligent document analysis
- **PyPDF2** - PDF text extraction
- **python-docx** - Word document processing
- **Threading** - Asynchronous file processing

### Frontend
- **Alpine.js** - Reactive JavaScript framework
- **HTML5/CSS3** - Modern, responsive design
- **Fetch API** - AJAX requests

## 📋 Prerequisites

- Python 3.7+
- OpenAI API key
- pip (Python package manager)

## 🚀 Installation

1. **Clone or download the repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure OpenAI API Key**
   
   Open [app.py](app.py) and replace the placeholder API key with your own:
   ```python
   openai.api_key = "your-openai-api-key-here"
   ```
   
   ⚠️ **Security Note**: Never commit your API key to version control. Consider using environment variables:
   ```python
   import os
   openai.api_key = os.getenv("OPENAI_API_KEY")
   ```

4. **Create uploads directory** (optional - automatically created on startup)
   ```bash
   mkdir uploads
   ```

## 💻 Usage

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   
   Navigate to `http://localhost:5000`

3. **Upload documents**
   - Click the file input to select files or drag and drop
   - Supported formats: `.pdf`, `.doc`, `.docx`
   - Multiple files can be uploaded at once

4. **Ask questions**
   - After upload completes, an input box will appear
   - Type your question about the uploaded documents
   - The AI will analyze the document content and provide answers
   - Responses animate word-by-word for better readability

## 📁 Project Structure

```
alpine_flask_file_upload_using_thread/
│
├── app.py                          # Main Flask application
├── app2.py                         # Alternative/backup implementation
├── requirements.txt                # Python dependencies
├── utils.py                        # Utility functions
├── products.json                   # Sample data file
├── test_Open_AI.py                # OpenAI API test script
│
├── templates/
│   ├── index.html                  # Main UI with Alpine.js
│   └── old.html                    # Previous version
│
├── uploads/                        # Uploaded files storage (created at runtime)
│
└── *.ipynb                         # Jupyter notebooks for OpenAI prompt engineering
    ├── Chat-bot.ipynb
    ├── Summarizing.ipynb
    ├── Transforming.ipynb
    ├── Inferring.ipynb
    ├── Expanding.ipynb
    ├── Process Inputs Chain of Thought Reasoning.ipynb
    └── Evaluation*.ipynb
```

## 🔄 How It Works

1. **File Upload**: User selects PDF/Word documents through the web interface
2. **Text Extraction**: Backend extracts text content using PyPDF2 and python-docx
3. **Threaded Processing**: Files are saved to disk using separate threads for each file
4. **Status Polling**: Frontend polls the backend every second for upload progress
5. **AI Interaction**: Once complete, users can ask questions about the uploaded documents
6. **Contextual Responses**: OpenAI API uses extracted text as context to answer queries

## 🎓 Additional Resources

This project includes several Jupyter notebooks demonstrating OpenAI prompt engineering techniques:

- **Chat-bot.ipynb** - Building conversational AI
- **Summarizing.ipynb** - Text summarization techniques
- **Transforming.ipynb** - Text transformation and formatting
- **Inferring.ipynb** - Sentiment analysis and information extraction
- **Expanding.ipynb** - Content generation and expansion
- **Process Inputs (Chain of Thought Reasoning).ipynb** - Advanced reasoning patterns
- **Evaluation*.ipynb** - Testing and evaluating AI outputs

These notebooks serve as learning materials and can help you understand the prompting patterns used in the main application.

## 🔧 Configuration

### Change Upload Folder
Edit `UPLOAD_FOLDER` in [app.py](app.py):
```python
UPLOAD_FOLDER = "your_custom_folder"
```

### Adjust Processing Delay
Modify the sleep duration in [app.py](app.py):
```python
time.sleep(10)  # Current: 10 seconds
```

### Switch AI Model
Change the model in [app.py](app.py):
```python
response = openai.ChatCompletion.create(
    model="gpt-4",  # or gpt-3.5-turbo
    # ...
)
```

## ⚠️ Important Notes

- **API Costs**: OpenAI API usage incurs costs. Monitor your usage at https://platform.openai.com/usage
- **File Size Limits**: Large files may take longer to process
- **API Rate Limits**: Be aware of OpenAI's rate limiting policies
- **Security**: Remove or secure your API key before deploying to production
- **File Storage**: Uploaded files persist in the `uploads/` directory

## 🐛 Troubleshooting

**Upload fails**:
- Check file format is supported (.pdf, .doc, .docx)
- Ensure `uploads/` directory has write permissions

**AI responses fail**:
- Verify OpenAI API key is valid
- Check API quota and billing status
- Review error messages in browser console

**Files not processing**:
- Check terminal for error messages
- Ensure all dependencies are installed correctly
- Verify Python version compatibility

## 📝 License

This project is provided as-is for educational and development purposes.

## 🤝 Contributing

Feel free to fork, modify, and improve this project according to your needs.

---

**Made with ❤️ using Flask, Alpine.js, and OpenAI**
