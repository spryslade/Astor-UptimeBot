FROM python:3.10.4
RUN apt-get update -y && apt-get upgrade -y
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD python3 meow.py
