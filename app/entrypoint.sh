#!/bin/sh
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

python manage.py collectstatic --no-input --clear
pybabel compile -i locale/ru/LC_MESSAGES/django.po -o locale/ru/LC_MESSAGES/django.mo -f
python manage.py makemigrations --no-input
python manage.py migrate

exec "$@"
