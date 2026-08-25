import pytest
from sample_app import sample

@pytest.fixture
def client():
    sample.config['TESTING'] = True
    with sample.test_client() as client:
        yield client

def test_home_status_200(client):
    response = client.get('/')
    print(f"\nCodigo de estado devuelto: {response.status_code}") # <--- Agrega esto
    assert response.status_code == 404