# Usamos una imagen liviana de Python
FROM python:3.10-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copiamos el archivo de requerimientos e instalamos librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código del proyecto
COPY . .

# Comando para arrancar el monitor
CMD ["python", "main.py"]