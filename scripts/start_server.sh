#!/bin/bash
cd /home/ubuntu/my-blog
source venv/bin/activate
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx