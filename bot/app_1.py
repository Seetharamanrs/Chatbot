from openai import OpenAI
import os 
from dotenv import load_dotenv 

load_dotenv()

prompt=   f""" 
 You are help assistant. Please response to the user queries
 Question:{question}
 Instructions:
 1. Speak Polite
 2. Don't not hallucinate 
""" 
client=OpenAI(api_key=api_key)

def generate_answer(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response
 