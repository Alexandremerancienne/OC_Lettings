FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBUG=0
ENV PORT 8000

EXPOSE 8000

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --clear

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
