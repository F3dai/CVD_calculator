FROM python:3.8-slim-buster

WORKDIR /app

EXPOSE 8000

RUN apt-get update && apt-get install libssl-dev build-essential default-libmysqlclient-dev nano -y

COPY . .
RUN pip install -r requirements.txt

ENV FLASK_APP=cvd_app
ENV FLASK_ENV=development

# Replace db connection to container if running as dockerfile
RUN sed -i "s|localhost|db|g" cvd_app/modules/db.py

#Run the container
CMD [ "flask", "run", "--host=0.0.0.0"]
