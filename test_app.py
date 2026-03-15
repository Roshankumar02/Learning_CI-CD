import sys
import os
# testing
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask_todo.app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
