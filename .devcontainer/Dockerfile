FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

RUN apt-get update && \
    apt-get install -y default-jre

RUN pip install kafka-python && \
    pip install customerio