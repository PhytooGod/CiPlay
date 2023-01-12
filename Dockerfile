 # Pull base image
FROM python:3.8-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
