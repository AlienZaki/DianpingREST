#!/bin/sh

gunicorn DianpingREST.wsgi --bind=0.0.0.0:80