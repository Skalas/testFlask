from app import app
import pytest
from flask import json, jsonify


def test_empty_db():
    """Start with a blank database."""
    rv = app.test_client().get('/')
    print(rv)
    assert b'<p>Hello, OPI!</p>' in rv.data


def test_add():
    response = app.test_client().post(
        '/truepost',
        data=json.dumps({'username': "Miguel", 'email': 'm.escalante@opianalytics.com'}),
        content_type='application/json',
    )
    print(response.data)
    assert response.status_code == 200
    assert b'{"email": "m.escalante@opianalytics.com", "username": "Miguel"}' in response.data
