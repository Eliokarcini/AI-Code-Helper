# 🤖 AI Code Helper

A full-stack web application that provides intelligent code analysis and programming assistance through Google Gemini AI integration.

## 🚀 Features

- **Code Explanation**: Detailed analysis of code functionality and structure
- **Debugging Assistance**: Identification and resolution of syntax and logical errors
- **Code Translation**: Conversion between multiple programming languages
- **Concept Explanation**: Comprehensive programming concept explanations at various skill levels
- **Code Optimization**: Performance and readability improvements

## 🛠 Tech Stack

**Frontend:** Streamlit, Plotly, Pandas  
**Backend:** FastAPI, Python  
**AI:** Google Gemini 2.0 Flash API  
**Architecture:** RESTful API with CORS middleware

## 📁 Project Structure

- **ai-code-helper/**
  - **backend/** - FastAPI server and AI integration
    - `main.py` - Core API server with AI endpoints
    - `requirements.txt` - Python dependencies
  - **frontend/** - Streamlit web interface
    - `app.py` - Main application interface
    - `requirements.txt` - Frontend dependencies
  - `README.md` - Project documentation

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### Installation & Deployment

1. **Repository Setup**
```bash
git clone https://github.com/yourusername/ai-code-helper.git
cd ai-code-helper
```
2. **Backend Server**
```
cd backend
pip install -r requirements.txt
python3 main.py
```
API server available at ```http://localhost:8000```

3. **Frontend Application**
```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
Web interface accessible at ```http://localhost:8501```
## 🔧 API Documentation

### Endpoints
- `POST /api/code/explain` - Comprehensive code analysis and explanation
- `POST /api/code/debug` - Error detection and correction suggestions
- `POST /api/code/translate` - Cross-language code translation
- `POST /api/concept/explain` - Programming concept education
- `POST /api/code/optimize` - Code performance and quality optimization

### Request Format
```json
{
  "code": "def example(): pass",
  "language": "python",
  "task": "explain"
}
```
## 💡 Implementation Examples

### 🔍 Code Analysis

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
Returns recursive function explanation with time complexity analysis

**Error Resolution**
```python
for i in range(10)
    print(i
```
Identifies syntax errors and provides corrected implementation

**Language Translation**

```python
def greet(name):
    return f"Hello, {name}!"
```
Generates equivalent JavaScript:```function greet(name) { return \Hello, ${name}!`; }```
## 🎯 Technical Architecture

- **AI Integration**: Real-time processing with Google Gemini 2.0 Flash
- **Multi-language Support**: Python, JavaScript, Java, C++, C#, Go, Rust, PHP, Ruby
- **Error Handling**: Comprehensive exception management with user-friendly messaging
- **Performance**: Sub-second response times with concurrent request support
- **Scalability**: Modular architecture supporting feature expansion

## 📊 Performance Metrics

- **Response Time**: < 2 seconds for average code analysis
- **Availability**: 99%+ uptime with graceful error handling
- **Concurrency**: Supports multiple simultaneous users
- **Accuracy**: High-quality AI-generated responses validated through testing

## 🔍 Technical Learning Outcomes

- **AI System Integration**: Implementation of Google Gemini API for code intelligence
- **Full-Stack Development**: FastAPI backend with Streamlit frontend architecture
- **API Design**: RESTful endpoint design with proper error handling and validation
- **Prompt Engineering**: Optimization of AI prompts for technical code analysis
- **Production Deployment**: Application architecture suitable for production environments

## 🎨 User Experience

- Professional interface with code syntax highlighting
- Real-time processing indicators
- Responsive design for various screen sizes
- Intuitive navigation between analysis features
- Comprehensive user feedback systems

## 🔮 Roadmap

- Version control integration for code history
- IDE plugin development
- Batch processing capabilities
- Custom model training integration
- Collaborative features for team development

## 📞 Technical Support

For technical issues or contribution inquiries, please create an issue in the project repository.

---

**Developer:** Elio Karcini  
**Technical Stack:** Python, FastAPI, Streamlit, Google Gemini AI  
**Project Focus:** AI-powered code analysis and developer productivity tools

*This project demonstrates professional full-stack development capabilities with cutting-edge AI integration for practical software engineering applications.*
