FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
COPY ./requirements.txt /tmp/

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
