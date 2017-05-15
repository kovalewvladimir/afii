#!/bin/bash

cd /opt/afii/
source ./bin/activate
cd /opt/afii/afii/
nohup python manage.py runserver 0.0.0.0:8000 >> /opt/afii/afii.log &
deactivate
