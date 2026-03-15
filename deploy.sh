#!/bin/bash

echo "Starting deployment..."

python3 -m venv deployenv
source deployenv/bin/activate

pip install dist/*.whl

python -m flask_todo.app
