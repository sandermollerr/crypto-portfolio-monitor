# Flask/Dash app Dockerfile
FROM python:3.8

RUN apt-get update

COPY requirements.txt .
RUN pip install \
    --no-cache-dir \
    --no-warn-script-location \
    --user \
    -r requirements.txt \
