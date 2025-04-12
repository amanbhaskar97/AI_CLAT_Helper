import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env


class GeminiChatbot:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.context = self.load_context()
        self.model = self.setup_gemini_model()

    def setup_gemini_model(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY not found. Please set it in your .env file.")

        try:
            configure(api_key=api_key)
            return GenerativeModel("gemini-2.0-flash")
        except Exception as e:
            raise RuntimeError(f"❌ Failed to configure Gemini model: {e}")

    def load_context(self):
        context_text = ""
        for filename in os.listdir(self.data_dir):
            filepath = os.path.join(self.data_dir, filename)
            if filename.endswith(".txt"):
                with open(filepath, "r", encoding="utf-8") as file:
                    context_text += file.read() + "\n"
        return context_text

    def get_answer(self, query):
        prompt = f"""
        You are a legal exam assistant. Use the following context to answer the question:
        
        Context:
        {self.context}

        Question: {query}
        """
        response = self.model.generate_content(prompt)
        return response.text.strip()
