import pytest
# IMPORTANTE: Reemplaza 'sample_app' por el nombre de tu archivo de Flask (ej. de sample_app import sample_app)
from sample_app import sample_app 

@pytest.fixture
def client():
    sample_app.config['TESTING'] = True
    with sample_app.test_client() as client:
        yield client

def test_home_status_200(client):
    """
    Prueba unitaria que simula una petición GET a la ruta '/'
    y valida estrictamente que responda con código HTTP 200 OK.
    """
    response = client.get('/')
    assert response.status_code == 200


