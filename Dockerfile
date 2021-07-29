FROM python:3.8.1-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
COPY . /app
EXPOSE 8080
RUN chmod +x gunicorn_server.sh
ENTRYPOINT ["./gunicorn_server.sh"]