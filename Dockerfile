FROM python:3.8-slim-buster
COPY . /src
WORKDIR /src
RUN apt-get update
RUN pip install -r flaskapp/requirements.txt
WORKDIR /src/nodeapp
RUN apt-get install npm -y
RUN npm install -y
WORKDIR /src
RUN python flaskapp/app.py &
WORKDIR /src/nodeapp
EXPOSE 5000 5001
WORKDIR /src
CMD ["bash","run.sh"]
