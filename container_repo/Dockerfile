FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_FRONTEND teletype

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y libreoffice
RUN yes | apt install -y ttf-mscorefonts-installer

WORKDIR /DOCX2PDF

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn" , "-b", "0.0.0.0:5000", "index:app"]

