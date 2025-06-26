import os
from dotenv import load_dotenv
from openai import OpenAI
from .prompts import messages_for
from .scraper import Website

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(url):
    website = Website(url)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_for(website)
    )
    return response.choices[0].message.content
