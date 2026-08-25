import pytest
# IMPORTANTE: Reemplaza 'app' por el nombre de tu archivo de Flask (ej. de app import app)
from app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_200(client):
    """
    Prueba unitaria que simula una petición GET a la ruta '/'
    y valida estrictamente que responda con código HTTP 200 OK.
    """
    response = client.get('/')
    assert response.status_code == 200


    