FROM python:3.7-alpine
LABEL description="Demo of client side inference with Tensorflow.js"

WORKDIR /app

RUN mkdir https
COPY https https/

COPY cat.png .
COPY cat2.jpg .
COPY index_cat.html .
COPY index_video.html .
COPY py_serv_https.py .

CMD [ "python3", "py_serv_https.py" ]