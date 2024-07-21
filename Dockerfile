FROM python:3.12.2

WORKDIR /docker_cont_crop_recom

LABEL org.opencontainers.image.authors="nigmucode@gmail.com"

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8002"]

