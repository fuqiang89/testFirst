#!/bin/sh

/python/virenv/bin/uwsgi --chdir=/var/www/testFirst --module=testFirst.wsgi:application --env DJANGO_SETTINGS_MODULE=testFirst.settings --master --pidfile=/etc/nginx/uwsgi.pid --socket=127.0.0.1:9000 --processes=5 --uid=1000 --gid=2000 --harakiri=20 --max-requests=5000 --vacuum --home=/python/virenv/  --daemonize=/var/log/uwsgi.log
