# Autor: Santiago Gonzalez Acevedo
# Descripcion: Docker para ejecutar servicios de IA

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 443

CMD ["python3", "main.py"]