#!/bin/bash

echo "Starting deployment..."

python3 -m venv deployenv
source deployenv/bin/activate

pip install -r requirements.txt

pip install dist/*.whl

python3 app.py
