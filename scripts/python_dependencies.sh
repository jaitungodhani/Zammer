#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip3 install psycopg2-binary
pip3 install -r /home/ubuntu/Zammer/requirements.txt
