FROM python:3.10-alpine

RUN apk add libreoffice-base \
    libreoffice \
    openjdk8-jre

WORKDIR /vercel-deploy

EXPOSE 5000
COPY requirements.txt .
COPY input input
COPY output output
COPY templates templates
COPY __init__.py __init__.py
COPY gunicorn_config.py gunicorn_config.py
COPY index.py index.py
COPY Procfile Procfile
COPY vercel.json vercel.json

RUN pip install -r requirements.txt
# COPY ./container_repo/ ./container_repo  This is throwing path error
# CMD ["gunicorn" , "-b", "0.0.0.0:5000", "container_repo.index:app"]  This is working fine
CMD ["gunicorn" , "-b", "0.0.0.0:5000", "index:app"]

