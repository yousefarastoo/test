FROM python:alpine 
RUN mkdir /app
COPY ./requirment.txt /app
RUN pip install -r requirment.txt
