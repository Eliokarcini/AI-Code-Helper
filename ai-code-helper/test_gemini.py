import google.generativeai as genai

API_KEY = "AIzaSyCB0euWyE5dBZDuElpZgCiE5me1IOx8Qao"

try:
    genai.configure(api_key=API_KEY)
    
    print("🚀 Testing available models...")
    
    # Test the models that are actually available
    test_models = [
        'models/gemini-2.0-flash',
        'models/gemini-2.0-flash-001', 
        'models/gemini-2.0-flash-lite',
        'models/gemini-2.0-flash-lite-001',
        'models/gemini-2.0-pro-exp',
        'models/gemini-flash-latest',
        'models/gemini-pro-latest'
    ]
    
    for model_name in test_models:
        try:
            print(f"Testing: {model_name}")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("Say 'Hello World' in Python code")
            print(f"✅ SUCCESS with {model_name}: {response.text[:100]}...")
            break
        except Exception as e:
            print(f"❌ {model_name} failed: {str(e)[:100]}...")
            
except Exception as e:
    print(f"❌ Overall error: {e}")