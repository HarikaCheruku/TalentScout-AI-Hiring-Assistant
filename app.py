import os
import streamlit as st
import requests
from dotenv import load_dotenv
from textblob import TextBlob
from googletrans import Translator
from functools import lru_cache
import time  # To add a timestamp for unique questions
import re

# Load environment variables
load_dotenv()
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face API URL (Using Llama 3 Model)
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Initialize translator
translator = Translator()

# Manually define supported languages (100+ languages)
supported_languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Italian": "it",
    "Korean": "ko",
    "Turkish": "tr",
    "Dutch": "nl",
    "Polish": "pl",
    "Vietnamese": "vi",
    "Thai": "th",
    "Greek": "el",
    "Swedish": "sv",
    "Czech": "cs",
    "Danish": "da",
    "Finnish": "fi",
    "Norwegian": "no",
    "Hebrew": "he",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Ukrainian": "uk",
    "Malay": "ms",
    "Indonesian": "id",
    "Filipino": "tl",
    "Urdu": "ur",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Punjabi": "pa",
    "Swahili": "sw",
    "Zulu": "zu",
    "Xhosa": "xh",
    "Afrikaans": "af",
    "Albanian": "sq",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Croatian": "hr",
    "Estonian": "et",
    "Farsi": "fa",
    "Galician": "gl",
    "Georgian": "ka",
    "Haitian Creole": "ht",
    "Icelandic": "is",
    "Irish": "ga",
    "Kazakh": "kk",
    "Kurdish": "ku",
    "Kyrgyz": "ky",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Mongolian": "mn",
    "Nepali": "ne",
    "Pashto": "ps",
    "Samoan": "sm",
    "Serbian": "sr",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Tajik": "tg",
    "Tatar": "tt",
    "Tongan": "to",
    "Uzbek": "uz",
    "Welsh": "cy",
    "Yiddish": "yi",
    "Yoruba": "yo",
    # Add more languages as needed
}

# Streamlit UI
st.set_page_config(page_title="TalentScout - AI Hiring Assistant 🤖", layout="centered")
st.title("🤖 TalentScout - AI Hiring Assistant")
st.write("Hello! I am your AI Hiring Assistant. Let's start by gathering some details.")

# Custom CSS to match the input box style from the image
st.markdown(
    """
    <style>
    /* Styling for all input fields */
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea, 
    .stNumberInput>div>div>input {
        background-color: #2E3348 !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border: 2px solid #FF4B4B !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }

    /* Styling for buttons */
    .stButton>button {
        background-color: #4CAF50 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
    }
    
    .stButton>button:hover {
        background-color: #45a049 !important;
    }

    /* Ensure markdown text is readable */
    .stMarkdown {
        font-family: 'Arial', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Collect Candidate Information
full_name = st.text_input("Full Name:")
email = st.text_input("Email Address:")
phone = st.text_input("Phone Number:")
experience = st.number_input("Years of Experience:", min_value=0, max_value=50, step=1)
position = st.text_input("Desired Position:")
location = st.text_input("Current Location:")
tech_stack = st.text_area("Enter your Tech Stack (Languages, Frameworks, Databases, Tools):")

# Language selection
language_name = st.sidebar.selectbox("Preferred Language:", list(supported_languages.keys()))
language_code = supported_languages[language_name]

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        return "😊 Positive"
    elif sentiment < 0:
        return "😠 Negative"
    else:
        return "😐 Neutral"

# Function to translate text using googletrans
def translate_text(text, target_language="en"):
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        return text  # Fallback to original text if translation fails

# Cache API calls
@lru_cache(maxsize=100)
def generate_questions_cached(tech_stack):
    # Add a timestamp to the prompt to ensure unique questions
    prompt = f"Generate 5 unique technical interview questions for a candidate skilled in {tech_stack}. Each question should be clear and concise. Do not provide answers or explanations. Timestamp: {time.time()}"

    payload = {"inputs": prompt}

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        result = response.json()

        if isinstance(result, list) and 'generated_text' in result[0]:
            questions = result[0]['generated_text'].split("\n")  # Split by lines
            return [q.strip() for q in questions if q.strip()]  # Clean extra spaces
        else:
            return ["❌ No questions generated. Try again with different tech stack keywords."]

    except Exception as e:
        return [f"⚠️ API Error: {str(e)}"]

# Function to remove leading numbers from a string
def remove_leading_numbers(text):
    return re.sub(r'^\d+\.\s*', '', text)

# Function to filter out irrelevant lines (e.g., answers or explanations)
def filter_questions(questions):
    filtered_questions = []
    for q in questions:
        # Skip lines that contain answers or explanations
        if "?" not in q and ":" not in q:
            continue
        filtered_questions.append(q)
    return filtered_questions

# Generate Questions Button
if st.button("Generate Technical Questions"):
    if tech_stack.strip():
        st.subheader("📌 Technical Questions")
        questions = generate_questions_cached(tech_stack)
        translated_questions = [translate_text(q, target_language=language_code) for q in questions]
        
        # Remove the first line (prompt) if it exists
        if len(translated_questions) > 0 and "Generate 5 unique technical interview questions" in translated_questions[0]:
            translated_questions = translated_questions[1:]
        
        # Filter out irrelevant lines (e.g., answers or explanations)
        filtered_questions = filter_questions(translated_questions)
        
        # Remove leading numbers and display questions as bullet points
        cleaned_questions = [remove_leading_numbers(q) for q in filtered_questions]
        st.markdown("\n".join([f"- {q}" for q in cleaned_questions]))

        # Ask for a review
        review = st.text_area("Please provide a review or feedback about the questions:")
        if review:
            sentiment = analyze_sentiment(review)
            st.write(f"**Sentiment Analysis**: {sentiment}")
    else:
        st.warning("⚠️ Please enter a tech stack to generate questions.")

st.write("Thank you for using TalentScout! Good luck with your job search! 🚀")