#!/bin/bash
# file: init.sh

# init project
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
