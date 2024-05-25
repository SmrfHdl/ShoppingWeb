FROM python:3.8-slim-buster

WORKDIR /app 

Add . /app

COPY requirements.txt requirements.txt
run pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]