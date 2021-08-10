FROM python:3.8.1-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
COPY . /app
RUN pip3 install -r requeriments.txt
EXPOSE 8080
RUN chmod +x start_gunicorn.sh
ENTRYPOINT ["sh", "./start_gunicorn.sh"]