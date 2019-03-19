FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY src ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD python papi.py
