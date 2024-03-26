FROM ubuntu:latest

# Actualiza la lista de paquetes disponibles e instala actualizaciones
RUN apt-get update && apt-get upgrade -y
#
# # Instala Python 3 y pip
RUN apt-get install -y python3 python3-pip
#
# # Instala herramientas adicionales
RUN apt-get install -y git
#
# # Opcional: Instalación de virtualenv
RUN pip3 install virtualenv
#
# # Clona tu repositorio
RUN git clone https://github.com/cristianmontesz/Proyecto_reflex.git /Proyecto_reflex
#
# # Define el directorio de trabajo dentro del contenedor
WORKDIR /App_reflex
#
# # Opcional: Crea un entorno virtual y actívalo
RUN virtualenv venv
ENV PATH="/Proyecto_reflex/venv/bin:$PATH"
#
# # Instala las dependencias de tu proyecto
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
#
# # Copia el resto de tu proyecto
COPY . .
#
# # Comando para ejecutar el script Python
CMD ["python3", "/Proyecto_reflex/App_reflex/App_reflex.py"]
