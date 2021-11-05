FROM python:3.10.0

ADD . /flask-api
WORKDIR /flask-api

COPY docker-entrypoint.py /docker-entrypoint.py

RUN chmod +x /docker-entrypoint.py
RUN pip3 install -r requirements.txt

CMD ["python", "/docker-entrypoint.py" ]