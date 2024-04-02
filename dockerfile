# Usa una imagen base de Python 3.8 en Ubuntu
FROM ubuntu:latest

# Actualiza los repositorios e instala las dependencias necesarias
RUN apt-get update && \
    apt-get install -y curl \
        gcc \
        python3-dev \
        python3-pip \
        musl-dev \
        libgirepository1.0-dev \
        linux-headers-generic \
        libffi-dev \
        libssl-dev \
        libcairo2-dev \
        libsystemd-dev \
        pkg-config \
        gir1.2-gtk-3.0 \
        libpango1.0-dev \
        python3-venv \
        libdbus-1-dev \
        libglib2.0-dev \
        git \
        unzip && \
    rm -rf /var/lib/apt/lists/*

#Eliminando repositorio
RUN rm -rf /Proyecto_reflex

## Crea el directorio de trabajo dentro del contenedor
WORKDIR /App_reflex

# Instalación opcional de virtualenv y activación
RUN python3 -m venv .venv

# Copia los archivos de requerimientos al directorio de trabajo
COPY requirements.txt .
COPY requirements_current.txt .

# Instala las dependencias de tu proyecto, incluyendo Reflex
# Asegúrate de activar el entorno virtual y luego instalar las dependencias
RUN . .venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt -r requirements_current.txt

# Clona tu repositorio (ajusta según necesidad)
RUN git clone https://github.com/cristianmontesz/Proyecto_reflex.git /Proyecto_reflex

# Copia el resto de tu proyecto (ajusta según necesidad)
COPY . .
## Instala las dependencias de tu proyecto, incluyendo Reflex
RUN pip install --upgrade pip
# Instala reflex
RUN pip install reflex
# Inicia reflex
RUN reflex init

# Exponer el puerto que utiliza tu aplicación
EXPOSE 3000

# Ejecuta tu aplicación Reflex
# # Ejecutar la aplicación en modo producción cuando el contenedor se inicie
CMD ["reflex", "run", "--env", "prod"]

