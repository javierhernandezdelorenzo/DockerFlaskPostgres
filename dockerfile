FROM python:3.8-slim-buster
RUN pip install --upgrade pip
RUN pip install --upgrade requests
RUN apt-get update
RUN apt-get install postgresql-client -y
RUN mkdir -p app
COPY  ./app /app
RUN pip install -r ./app/requirements.txt
WORKDIR /app
EXPOSE 5000
ENV FLASK_APP /app/app.py
#CMD ["python3", "app.py", "--port", "5000"]

