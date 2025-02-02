FROM python:3.11.5-slim-bullseye

RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get clean

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/
COPY static /app/static/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]