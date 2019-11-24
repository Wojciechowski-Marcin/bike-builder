FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install numpy
RUN pip install --upgrade pip -r requirements.txt

ADD . /app/

COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

