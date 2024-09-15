FROM python:3.11

WORKDIR /usr/src/rag_chat

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /web .
