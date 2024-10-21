FROM python:3.8-slim

RUN pip install apache-flink kafka-python

COPY main.py /app/main.py
WORKDIR /app

CMD ["python", "main.py"]