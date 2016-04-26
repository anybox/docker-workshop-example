FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY server.py /usr/src/app/


ENV COUNTER_PATH "/data/counter.txt"
RUN mkdir -p $(dirname $COUNTER_PATH) && \
    echo "0" > $COUNTER_PATH

EXPOSE 8080
VOLUME /data
CMD ["python3", "server.py"]
