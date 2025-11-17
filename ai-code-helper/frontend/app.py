import streamlit as st
import requests
import json
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="AI Code Helper",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API configuration
API_BASE_URL = "http://localhost:8000/api"

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .code-block {
        background-color: #272822;
        color: #f8f8f2;
        padding: 1rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
    }
    .response-box {
        background-color: #e8f4fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

def call_api(endpoint, data):
    """Helper function to call API endpoints"""
    try:
        response = requests.post(f"{API_BASE_URL}/{endpoint}", json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {str(e)}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Code Helper</h1>', unsafe_allow_html=True)
    st.markdown("Your intelligent programming assistant for code explanation, debugging, and optimization.")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    feature = st.sidebar.radio(
        "Choose a feature:",
        ["Code Explanation", "Debug Code", "Translate Code", "Explain Concept", "Optimize Code"]
    )
    
    # Feature descriptions
    feature_descriptions = {
        "Code Explanation": "Understand what any code does with detailed explanations",
        "Debug Code": "Find and fix errors in your code",
        "Translate Code": "Convert code between programming languages",
        "Explain Concept": "Learn programming concepts with examples",
        "Optimize Code": "Improve code performance and readability"
    }
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Current Feature:** {feature}")
    st.sidebar.markdown(feature_descriptions[feature])
    
    # Main content area based on selected feature
    if feature == "Code Explanation":
        render_code_explanation()
    elif feature == "Debug Code":
        render_debug_code()
    elif feature == "Translate Code":
        render_translate_code()
    elif feature == "Explain Concept":
        render_explain_concept()
    elif feature == "Optimize Code":
        render_optimize_code()

def render_code_explanation():
    st.header("🔍 Code Explanation")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Input Your Code")
        language = st.selectbox(
            "Programming Language",
            ["python", "javascript", "java", "c++", "c#", "go", "rust", "php", "ruby"],
            key="explain_lang"
        )
        
        code_input = st.text_area(
            "Paste your code here:",
            height=300,
            placeholder="def hello_world():\n    print('Hello, World!')\n\nhello_world()",
            key="explain_code"
        )
    
    with col2:
        st.subheader("Explanation")
        if st.button("Explain Code", type="primary", use_container_width=True):
            if code_input.strip():
                with st.spinner("Analyzing your code..."):
                    result = call_api("code/explain", {
                        "code": code_input,
                        "language": language,
                        "task": "explain"
                    })
                    
                    if result and result.get("success"):
                        st.markdown("### 📖 Code Explanation")
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown(result["explanation"])
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Display the original code
                        st.markdown("### 📝 Your Original Code")
                        st.code(code_input, language=language)
            else:
                st.warning("Please enter some code to explain.")

def render_debug_code():
    st.header("🐛 Debug Code")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Code with Issues")
        language = st.selectbox(
            "Programming Language",
            ["python", "javascript", "java", "c++", "c#", "go", "rust", "php", "ruby"],
            key="debug_lang"
        )
        
        code_input = st.text_area(
            "Paste the code that needs debugging:",
            height=300,
            placeholder="# Example buggy code\nfor i in range(10)\n    print(i",
            key="debug_code"
        )
    
    with col2:
        st.subheader("Debugging Results")
        if st.button("Find and Fix Errors", type="primary", use_container_width=True):
            if code_input.strip():
                with st.spinner("Looking for bugs..."):
                    result = call_api("code/debug", {
                        "code": code_input,
                        "language": language,
                        "task": "debug"
                    })
                    
                    if result and result.get("success"):
                        st.markdown("### 🔧 Debugging Analysis")
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown(result["debug_info"])
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter some code to debug.")

def render_translate_code():
    st.header("🌐 Translate Code")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Source Code")
        source_lang = st.selectbox(
            "From Language",
            ["python", "javascript", "java", "c++", "c#", "go", "rust", "php", "ruby"],
            key="source_lang"
        )
        
        code_input = st.text_area(
            "Code to translate:",
            height=250,
            placeholder="def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
            key="translate_code"
        )
    
    with col2:
        st.subheader("Translation")
        target_lang = st.selectbox(
            "To Language",
            ["python", "javascript", "java", "c++", "c#", "go", "rust", "php", "ruby"],
            key="target_lang"
        )
        
        if st.button("Translate Code", type="primary", use_container_width=True):
            if code_input.strip():
                with st.spinner("Translating code..."):
                    result = call_api("code/translate", {
                        "code": code_input,
                        "language": source_lang
                    })
                    
                    if result and result.get("success"):
                        st.markdown("### 🔄 Translated Code")
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown(result["translation"])
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter some code to translate.")

def render_explain_concept():
    st.header("📚 Explain Programming Concept")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Concept Details")
        concept = st.text_input(
            "Programming Concept:",
            placeholder="e.g., recursion, object-oriented programming, async/await",
            key="concept_input"
        )
        
        level = st.selectbox(
            "Explanation Level",
            ["beginner", "intermediate", "advanced"],
            key="concept_level"
        )
    
    with col2:
        st.subheader("Explanation")
        if st.button("Explain Concept", type="primary", use_container_width=True):
            if concept.strip():
                with st.spinner("Generating explanation..."):
                    result = call_api("concept/explain", {
                        "concept": concept,
                        "level": level
                    })
                    
                    if result and result.get("success"):
                        st.markdown("### 💡 Concept Explanation")
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown(result["explanation"])
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter a programming concept to explain.")

def render_optimize_code():
    st.header("⚡ Optimize Code")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Original Code")
        language = st.selectbox(
            "Programming Language",
            ["python", "javascript", "java", "c++", "c#", "go", "rust", "php", "ruby"],
            key="optimize_lang"
        )
        
        code_input = st.text_area(
            "Code to optimize:",
            height=300,
            placeholder="# Example: Inefficient Fibonacci\ndef fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)",
            key="optimize_code"
        )
    
    with col2:
        st.subheader("Optimized Version")
        if st.button("Optimize Code", type="primary", use_container_width=True):
            if code_input.strip():
                with st.spinner("Optimizing your code..."):
                    result = call_api("code/optimize", {
                        "code": code_input,
                        "language": language,
                        "task": "optimize"
                    })
                    
                    if result and result.get("success"):
                        st.markdown("### 🚀 Optimization Results")
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown(result["optimization"])
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter some code to optimize.")

if __name__ == "__main__":
    main()