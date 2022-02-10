FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace
COPY requirements.txt /workspace/

RUN pip install -r requirements.txt
RUN pip install --upgrade pip
ADD . /workspace/
