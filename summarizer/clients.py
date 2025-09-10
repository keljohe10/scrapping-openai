import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_openai_client():
    """Inicializa y retorna el cliente de OpenAI con la API key."""
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_llama_client():
    """Inicializa y retorna el cliente de OpenAI configurado para Ollama."""
    return OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
