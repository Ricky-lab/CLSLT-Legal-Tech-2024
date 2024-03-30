# ai_model.py
from langchain_community.chat_models import ChatOpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

def get_ai_response(user_input):
    try:
        formatted_input = [{"role": "user", "content": user_input}]
        response = llm.generate(formatted_input)
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I could not process your request."
