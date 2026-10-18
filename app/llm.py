from openai import OpenAI
from .config import OPENAI_API_KEY,OPENAI_MODEL

class LLMGenerator:
    def __init__(self):
        if not OPENAI_API_KEY: raise ValueError("OPENAI_API_KEY is missing")
        self.client=OpenAI(api_key=OPENAI_API_KEY)
    def generate(self,prompt:str)->str:
        r=self.client.responses.create(model=OPENAI_MODEL,input=prompt)
        return r.output_text.strip()
