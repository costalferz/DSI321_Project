FROM python:3.8.10-slim
WORKDIR /code
COPY . .
COPY requirements.txt  requirements.txt
RUN pip install -r /code/requirements.txt