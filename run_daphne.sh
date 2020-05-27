#!/bin/sh

if [ -f camera_site/local_settings.py ]
then
    export DJANGO_SETTINGS_MODULE=camera_site.local_settings
fi

daphne -u site.sock camera_site.asgi:application

