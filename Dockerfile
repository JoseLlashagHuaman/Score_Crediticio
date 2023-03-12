

FROM python:3.10

#Instalar el entorno virtual
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

#Carpeta del aplicativo
WORKDIR /app
ADD . /app

#Instalar las dependencias y los requirements
RUN apt-get update && apt-get install -y libgomp1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --pre pycaret

EXPOSE 5000

#Correr aplicación
CMD ["python", "app.py"]
