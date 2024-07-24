FROM python:3.12.2

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

LABEL org.opencontainers.image.authors="nigmucode@gmail.com"

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT [ "gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]

