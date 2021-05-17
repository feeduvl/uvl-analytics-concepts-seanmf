FROM python:3.8-slim-buster

RUN pip3 install --upgrade pip \
    Flask==1.0.2 \
    numpy==1.20.3 \


EXPOSE 9657

CMD [ "python3", "./starter.py" ]