FROM python:3-alpine

RUN apk --update add \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libxml2-dev \
    libxslt-dev

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY app /usr/src/app/
RUN cd business/ && \
    python3 setup.py install && \
    cd ../service && \
    python3 /usr/src/app/service/setup.py install

COPY anyblok.cfg /usr/src/app/

EXPOSE 8080
CMD ["anyblok_pyramid", "-c", "anyblok.cfg"]
