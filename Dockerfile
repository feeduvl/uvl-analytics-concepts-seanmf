FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade pip -r requirements.txt

COPY . .

EXPOSE 9657

CMD [ "python3", "./starter.py" ]