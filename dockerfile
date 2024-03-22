FROM ubuntu:latest

# Actualiza la lista de paquetes disponibles e instala actualizaciones
RUN apt-get update && apt-get upgrade -y

# Instala Python 3
RUN apt-get install -y python3

# Instala pip
RUN apt-get install -y python3-pip

# Instala reflex
RUN apt-get install -y reflex

## Instala git
RUN apt-get install -y git
                                               
## Elimina los paquetes que ya no son necesarios

RUN apt autoremove -y

RUN git clone https://github.com/cristianmontesz/Proyecto_reflex.git

# Define el directorio de trabajo dentro del contenedor

WORKDIR /Proyecto_reflex

RUN pip3 install -r requirements.txt

# Comando para ejecutar el script Python
CMD python3 /Proyecto_reflex/App_reflex/App_reflex.py
