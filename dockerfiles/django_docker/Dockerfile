FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace

#ER図を出力するのに必要なライブラリ
RUN apt-get update -y
RUN apt-get dist-upgrade -y
RUN apt-get install -y build-essential graphviz-dev graphviz pkg-config

COPY requirements.txt /workspace/
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
ADD . /workspace/
