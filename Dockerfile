FROM python:3.8.16-slim-bullseye
WORKDIR /code
COPY . /code
COPY requirements.txt  requirements.txt
RUN pip install -r /code/requirements.txt
