#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"

python3 manage.py migrate --noinput

echo "Waiting for webinstaller to finish..."
while ping -c 1 webinstaller > /dev/null; do
    sleep 0.1
done
echo "Webinstaller exited"

python3 manage.py collectstatic --noinput
python3 manage.py check --deploy

exec "$@"
