FROM python:3.7.0

WORKDIR /application
COPY * /application/
RUN pip install -r requirements.txt &&\
    rm -f Dockerfile &&\
    rm -f requirements.txt
