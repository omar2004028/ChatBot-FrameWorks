# Imagen base
FROM python:3.12

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del backend
COPY ./app ./app
COPY requirements.txt .
COPY .env .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para arrancar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
