import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY bulunamadı")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

def chat():
    print("Gemini AI hazır. Çıkmak için 'exit'")
    while True:
        prompt = input(">> ")
        if prompt.lower() == "exit":
            break

        response = model.generate_content(prompt)
        print(response.text)

if __name__ == "__main__":
    chat()
