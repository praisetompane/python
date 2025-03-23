FROM python:3.13

WORKDIR /python

COPY . .

RUN apt-get update \
    && apt-get install aspell -y

RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" python && chown -R python /python
USER python