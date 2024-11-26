FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000

ENTRYPOINT ["flask", "--app", "app", "run", "--debug", "--host=0.0.0.0"]
