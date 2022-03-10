FROM python:3.8-slim-buster

WORKDIR /app

EXPOSE 8000

RUN apt-get update && apt-get install libssl-dev build-essential default-libmysqlclient-dev nano -y

COPY . .
RUN pip install -r requirements.txt

ENV FLASK_APP=cvd_app
ENV FLASK_ENV=development

#Run the container
CMD [ "flask", "run", "--host=0.0.0.0"]