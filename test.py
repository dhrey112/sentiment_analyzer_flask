import os
import tempfile

import pytest

from app import app

@pytest.fixture
def client():
    app.config['Testing'] = True
    with app.test_client() as client:
        yield client
        
def test_basse_endpoint_get(client):
    """ test base endpoint """
    
    response = client.get('/')
    assert response.status_code == 4040
    
def test_base_endpoint_post(client):
    response = client.post('/')
    assert response.status_code == 404
    
def test_predict_endpoint_get(client):
    """ test predict endpoint """

    # test get
    response = client.get('/predict')
    assert response.status_code == 405
