# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .

RUN pip install

CMD ["python", "./main.py"]