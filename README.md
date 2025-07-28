# 🤖 ChatBot-FrameWorks

**ChatBot-FrameWorks** es un backend desarrollado con **FastAPI** que expone una API para interactuar con un chatbot basado en inteligencia artificial.

Actualmente se encuentra desplegado en Render:

🔗 https://chatbot-frameworks-page.onrender.com

---

## 🚀 Tecnologías usadas

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- OpenRouter API (para conexión con modelos de IA)
- Render (hosting)

---

## 🧠 IA mediante OpenRouter

El backend está integrado con la API de [OpenRouter](https://openrouter.ai/), permitiendo enviar mensajes y obtener respuestas de modelos como GPT-4, Claude, Mistral, entre otros.

- Las peticiones se hacen vía HTTP con autenticación Bearer.
- La clave se gestiona con una variable de entorno segura.

```http
POST https://openrouter.ai/api/v1/chat/completions
Authorization: Bearer TU_API_KEY
Content-Type: application/json
```

## 👨‍💻 Developers

- [Omar Alejandro Cardenas Rojas](https://github.com/omar2004028)
- [Marlon Eduardo Parra Ruedas](https://github.com/Marlon-Parra)


---