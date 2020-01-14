FROM python:3.6.4-jessie

COPY ./ /src/
WORKDIR /src
RUN pip install -r requirements.txt
