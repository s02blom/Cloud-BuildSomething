FROM python:3.10-slim

WORKDIR /server

RUN apt update
RUN apt-get install pkg-config default-libmysqlclient-dev build-essential -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV DATABSE_USER root
ENV FLASK_RUN_PORT 5001
COPY . .
EXPOSE $FLASK_RUN_PORT

ENTRYPOINT ["flask", "--app", "server", "run", "--debug", "--host=0.0.0.0"]
