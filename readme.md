### Custom Assistant Project
- This is a simple chatbot application built using Langchain, Ollama LLM, and Streamlit. The bot responds to user queries on a custom topic by leveraging a pre-trained language model.

#### Features
- Interactive chatbot interface using Streamlit.
- Powered by Ollama’s `gemma3` model.
- Custom prompt template guiding the assistant’s responses.
- Environment variables used to manage API keys securely.
- Langchain framework for chaining prompt templates and LLM outputs.

Installation:

Install dependencies:
``` bash
pip install -r requirements.tx
```
Create a .env file and add your Langsmith API key:
```bash
LANGSMITH_API_KEY=your_api_key_here
```