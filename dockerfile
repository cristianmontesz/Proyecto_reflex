# Usa una imagen base de Ubuntu con Python 3.8 o superior
FROM python:3.8-alpine
# #
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers
# # # Actualiza la lista de paquetes disponibles e instala git
RUN apk update && apk add --no-cache git && rm -rf /var/cache/apk/*
# #
# # # Crea el directorio de trabajo dentro del contenedor
WORKDIR /Proyecto_reflex
# # # Opcional: Instalación de virtualenv y activación
RUN python3 -m venv .venv
# # # Nota: La activación del entorno virtual en Dockerfile con 'source' no es efectiva entre comandos RUN
# #
# # # Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .
# #
# # # Instala las dependencias de tu proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# # #
# # Instala las dependencias de tu proyecto, incluyendo Reflex
RUN pip install reflex
# # Elimina el directorio existente si está presente
RUN rm -rf /Proyecto_reflex
# # # Clona tu repositorio (ajusta según necesidad)
RUN git clone https://github.com/cristianmontesz/Proyecto_reflex.git /Proyecto_reflex
# #
# # # Copia el resto de tu proyecto (ajusta según necesidad)
COPY . .
# #
# # # Ejecuta tu aplicación
CMD ["python", "/Proyecto_reflex/App_reflex/App_reflex.py"]
