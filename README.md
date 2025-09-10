# 🕸️ Web Summarizer

Este proyecto en Python te permite extraer y resumir el contenido de cualquier página web utilizando la API de OpenAI. Ideal para periodistas, analistas, investigadores o cualquier persona que quiera obtener resúmenes rápidos de sitios web.

---

## 🚀 Características

- Scraping básico del contenido visible de una página web (sin scripts, estilos ni imágenes).
- Generación de resumen utilizando `gpt-4o-mini` (o el modelo que prefieras).
- Limpio y modular: fácil de mantener y escalar.

---

## 📁 Estructura del proyecto

```bash
web_summarizer/
├── .env                 # Tu clave API de OpenAI (nunca la subas a GitHub)
├── .gitignore           # Archivos y carpetas excluidos del repositorio
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Este archivo
├── main.py              # Punto de entrada del programa
└── summarizer/          # Lógica del proyecto
    ├── __init__.py
    ├── scraper.py
    ├── prompts.py
    └── openai_client.py
```

---

## ⚙️ Requisitos

- Python 3.8+
- Cuenta de OpenAI con una clave API válida

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/keljohe10/web_summarizer.git
cd web_summarizer
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configura tu clave API

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ **Nunca subas tu `.env` al repositorio.** Ya está listado en `.gitignore`.

---

## 🧪 Uso

Ejecuta el script principal:

```bash
python main.py
```

Ingresa una URL cuando se te solicite, por ejemplo:

```
Ingresa la URL del sitio web a resumir: https://anthropic.com
```

Y verás un resumen generado directamente en la terminal 🎯

---

## 🤖 Modelos compatibles

Este proyecto usa por defecto:

```python
model="gpt-4o-mini"
```

Puedes cambiarlo por `"gpt-3.5-turbo"` o el modelo que prefieras, siempre y cuando esté disponible en tu cuenta de OpenAI.

---

## 📝 Licencia

MIT License
