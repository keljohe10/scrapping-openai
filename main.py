from summarizer.openai_client import summarize

def main():
    url = input("Ingresa la URL del sitio web a resumir: ").strip()
    if not url:
        print("No ingresaste una URL válida.")
        return
    
    # Pedir al usuario que elija el modelo
    print("\n¿Qué modelo quieres usar?")
    print("1. OpenAI (gpt-4o-mini)")
    print("2. Llama (llama3.2)")
    
    while True:
        choice = input("Ingresa tu opción (1 o 2): ").strip()
        if choice == "1":
            model_type = "openai"
            break
        elif choice == "2":
            model_type = "llama"
            break
        else:
            print("Opción inválida. Por favor ingresa 1 o 2.")
    
    print(f"\nResumen de: {url}")
    print(f"Usando modelo: {model_type}")
    print("-" * 60)
    print(summarize(url, model_type))

if __name__ == "__main__":
    main()
