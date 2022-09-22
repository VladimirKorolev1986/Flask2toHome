import pytest
from api import db
from app import app
from config import Config


@pytest.fixture()
def application():
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': Config.TEST_DATABASE
    })
    db.create_all()
    yield app
    db.drop_all()


@pytest.fixture()
def client(application):
    return application.test_client()


# def test_user_get_by_id(client):
#     response = client.get('/users/1')
#     assert response.status_code == 200

def test_user_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == 404


def test_user_creation(client):
    user_data = {
        "username": 'admin',
        'password': 'admin'
    }
    response = client.post('/users',
                           json=user_data,
                           content_type='application/json')
    data = response.json
    assert response.status_code == 201
    assert 'admin' in data.values()
