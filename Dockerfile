FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /djongo_test
WORKDIR /djongo_test
COPY . /djongo_test/
RUN pip install -r requirements.txt