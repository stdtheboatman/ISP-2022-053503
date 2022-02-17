FROM python:3.11.0a5-alpine3.15

WORKDIR /app

COPY . .

ENV ARGS=""

CMD python3 main.py ${ARGS}