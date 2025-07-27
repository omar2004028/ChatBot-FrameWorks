from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
from openai import OpenAI
from app.config import PROMPT_SISTEMA
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Inicializar FastAPI
app = FastAPI()

#  Agrega el middleware CORS justo aquí
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # o "*" para permitir todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class Pregunta(BaseModel):
    pregunta: str

# Ruta principal
@app.post("/chat")
def obtener_respuesta(p: Pregunta):
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-small-3.1-24b-instruct:free",
            messages=[
                {"role": "system", "content": PROMPT_SISTEMA},
                {"role": "user", "content": p.pregunta}
            ]
        )
        return {"respuesta": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
