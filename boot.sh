#!/bin/bash
gunicorn fcu_shop.wsgi:application \
  --bind 127.0.0.1:8000 \
  --forwarded-allow-ips="*"
