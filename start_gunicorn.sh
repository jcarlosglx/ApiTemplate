#!/usr/sh
gunicorn --bind 0.0.0.0:8080 --threads 2 --workers 2 main:instance