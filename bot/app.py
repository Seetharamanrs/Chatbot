# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()
os.environ['LANGCHAIN_TRACKING_V2']='true'
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGSMITH_API_KEY')
LANGSMITH_PROJECT="pr-granular-descent-64"



prompt=ChatPromptTemplate(
    [
        ('system',"You are help assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
st.title("Custom Assistant Project")
input_text=st.text_input("Ask me anything about your topic")

llm=Ollama(model='gemma3')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))