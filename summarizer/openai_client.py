from .clients import get_openai_client, get_llama_client
from .prompts import messages_for
from .scraper import Website

def summarize(url, model_type="gpt-4o-mini"):
    website = Website(url)
    
    # Configurar el cliente según el tipo de modelo
    if model_type == "openai":
        client = get_openai_client()
        model_name = "gpt-4o-mini"
    elif model_type == "llama":
        client = get_llama_client()
        model_name = "llama3.2"
    else:
        raise ValueError("Modelo no soportado. Use 'openai' o 'llama'.")
    
    response = client.chat.completions.create(
        model=model_name,
        messages=messages_for(website)
    )
    return response.choices[0].message.content
