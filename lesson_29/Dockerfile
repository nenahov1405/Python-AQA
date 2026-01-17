FROM python:3.13

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

RUN pip install sqlalchemy psycopg2-binary pytest

COPY main.py .

CMD ["pytest", "main.py"]