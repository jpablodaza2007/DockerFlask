import pytest
from sample_app import sample

@pytest.fixture
def client():
    sample.config['TESTING'] = True
    with sample.test_client() as client:
        yield client

def test_home_status_200(client):
    """
    Prueba unitaria que simula una petición GET a la ruta '/'
    y valida estrictamente que responda con código HTTP 200 OK.
    """
    response = client.get('/')
    assert response.status_code == 200


