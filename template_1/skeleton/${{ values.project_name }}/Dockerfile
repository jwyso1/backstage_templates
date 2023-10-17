ARG PYTHON_VERSION="3.11"
FROM mcr.microsoft.com/vscode/devcontainers/python:${PYTHON_VERSION}

RUN apt-get update \
    && apt-get install git \
    && pip install --upgrade pip

COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt \
    && rm -f requirements_dev.txt
