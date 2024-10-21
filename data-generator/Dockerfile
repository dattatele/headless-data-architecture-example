FROM python:3.8-slim

RUN pip install kafka-python

COPY generate_data.py /app/generate_data.py
WORKDIR /app

CMD ["python", "generate_data.py"]