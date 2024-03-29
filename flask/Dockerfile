FROM python:3.9-slim-buster

WORKDIR /compose

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install Flask==3.0.2 Werkzeug==3.0.1


COPY . .

CMD ["python", "server.py"]
