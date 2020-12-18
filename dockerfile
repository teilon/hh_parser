# FROM tiangolo/uwsgi-nginx-flask:python3.7
# FROM alpine:3.7
FROM python:3.8

RUN mkdir app
WORKDIR /app

COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# RUN \
#  apk add --no-cache python3 postgresql-libs && \
#  apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
#  python3 -m pip install -r requirements.txt --no-cache-dir && \
#  apk --purge del .build-deps

COPY ./app /app/

ENV TZ Asia/Almaty
CMD ["python3", "app.py"]