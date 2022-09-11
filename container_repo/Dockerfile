FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_FRONTEND teletype

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y libreoffice
# Installing fonts is must for a accurate conversion or else libreoffice replaces the user fonts with some other inbuilt fonts as libreoffice in general don't have all the fonts like MS Office.
RUN yes | apt install -y ttf-mscorefonts-installer

WORKDIR /DOCX2PDF
# copy all the contents of the Dockerfile directory into the WORKDIR
COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn" , "-b", "0.0.0.0:5000", "index:app"]

