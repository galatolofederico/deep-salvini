FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py ./

COPY model /usr/src/model
ENV MODEL /usr/src/model

EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 server:app