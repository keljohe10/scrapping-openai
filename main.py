from summarizer.openai_client import summarize

def main():
    url = input("Ingresa la URL del sitio web a resumir: ").strip()
    if url:
        print(f"\nResumen de: {url}")
        print("-" * 60)
        print(summarize(url))
    else:
        print("No ingresaste una URL válida.")

if __name__ == "__main__":
    main()
