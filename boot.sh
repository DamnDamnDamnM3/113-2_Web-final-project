#!/bin/bash
clear

git config --global user.name "jw_albert"
git config --global user.email "ru04jo30801@gmail.com"

echo "Pulling latest code from Python branch"
#git pull origin Python
python3 manage.py runserver 0.0.0.0:8000
