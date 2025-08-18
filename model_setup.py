# model_setup.py
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_model():
    model_name = "llama-3.1-8b-instant"
    
    return ChatGroq(model=model_name)

