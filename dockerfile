FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
