#!/bin/bash
cd /home/ubuntu/my-blog
# python3 -m venv venv
source /home/ubuntu/my-blog/venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate