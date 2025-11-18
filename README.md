# ATS Resume Checker with Google Gemini 🤖

An intelligent ATS (Applicant Tracking System) Resume Checker powered by Google's Gemini AI that helps job seekers optimize their resumes for better job application success rates.

## 🌟 Features

- **Resume Analysis**: Get detailed professional evaluation of your resume against job descriptions
- **Skills Gap Identification**: Receive personalized advice on improving your skills
- **Keyword Extraction**: Identify key skills and keywords required for specific job roles
- **Match Percentage**: Calculate how well your resume matches a job description
- **Resume Optimization**: Get suggestions to align your resume with target job roles
- **Cover Letter Generation**: Create tailored cover letters based on your resume and job description

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Google API key for Gemini AI

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nihart1207/ATS-Checker-GoogleGemini.git
   cd ATS-Checker-GoogleGemini
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🔧 Getting Your Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and add it to your `.env` file

## 📖 How to Use

1. **Start the application** by running `streamlit run app.py`
2. **Enter a job description** in the text area
3. **Upload your resume** in PDF format
4. **Choose an analysis option**:
   - **Resume Details**: Get comprehensive resume analysis
   - **Skills Improvement**: Receive personalized skill development advice
   - **Key Skills**: Identify required skills for the job
   - **Match Percentage**: See how well your resume matches
   - **Resume Editing**: Get optimization suggestions
   - **Cover Letter**: Generate a tailored cover letter

## 🛠 Technical Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **PDF Processing**: PyMuPDF (fitz)
- **Image Processing**: Pillow (PIL)
- **Environment Management**: python-dotenv

## 📋 Dependencies

```
streamlit
Pillow
pymupdf
google-generativeai
python-dotenv
```

## 🎯 Supported Job Domains

The AI is specifically trained to analyze resumes for:
- Data Science
- Full Stack Web Development
- Big Data Engineering
- DevOps
- Data Analysis

## 📝 File Structure

```
ATS-Checker-GoogleGemini/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .env              # Environment variables (create this)
```

## 🔄 How It Works

1. **PDF Processing**: Converts the first page of your PDF resume to image format
2. **AI Analysis**: Uses Google Gemini to analyze the resume image against job descriptions
3. **Intelligent Prompting**: Employs specialized prompts for different types of analysis
4. **Result Generation**: Provides actionable insights and recommendations

## ⚠️ Limitations

- Currently processes only the first page of PDF resumes
- Requires stable internet connection for AI API calls
- PDF quality affects OCR accuracy

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Issues & Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/nihart1207/ATS-Checker-GoogleGemini/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your problem

## 🚀 Future Enhancements

- [ ] Multi-page PDF support
- [ ] Support for Word documents
- [ ] Resume scoring dashboard
- [ ] Industry-specific analysis
- [ ] Keyword density metrics
- [ ] Resume template suggestions
- [ ] Batch processing capabilities

---

**Made with ❤️ by [Nihar Tripathi](https://github.com/nihart1207)**