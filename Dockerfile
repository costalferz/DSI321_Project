FROM python:3.8.5-slim-buster
WORKDIR /code
COPY . .
COPY requirement.txt  requirement.txt
COPY .env-template .env 

RUN pip install -r /code/requirement.txt
# CMD RUN SCRIPY.py