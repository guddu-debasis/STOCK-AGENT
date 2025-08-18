from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def get_model():
    return ChatGoogleGenerativeAI(model="gemini-1.5-flash")
