# 🤖 ChatBot-FrameWorks

**ChatBot-FrameWorks** es un backend desarrollado con **FastAPI** que expone una API para interactuar con un chatbot basado en inteligencia artificial.

Actualmente se encuentra desplegado en Render:

🔗 https://chatbot-frameworks-page.onrender.com

⚠️ Advertencia, por favor tenga en cuenta que el Chatbot puede tardar en responder ya que esta subido en Render con su plan gratuito.

En caso de que el chatbot no responda de 30 a 60 segundos, refresque la pagina o cierre y vuelva a entrar.

Luego de que el Chatbot responda, quiere decir que el server de Render esta activo pero no por mucho tiempo. aproximadamente unos 15 minutos, luego de eso si no hay actividad el server se vuelve a dormir y tendra que esperar nuevamente a que el server arranque. 

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