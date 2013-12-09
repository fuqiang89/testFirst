#/bin/sh

pid=`cat /etc/nginx/uwsgi.pid`


kill -9 $pid
