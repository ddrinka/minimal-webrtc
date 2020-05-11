#!/bin/sh

export DJANGO_SETTINGS_MODULE=camera_site.local_settings
daphne -u site.sock camera_site.asgi:application

