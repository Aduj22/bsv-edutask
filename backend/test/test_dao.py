import pytest
from src.util.dao import DAO

@pytest.fixture
def test_dao():
    dao = DAO("user")

    dao.drop()

    yield dao

    dao.drop()


def test_create_valid(test_dao):
    data = {
        "firstName": "Cristiano",
        "lastName": "Ronaldo",
        "email": "ronaldo@example.com"
    }

    result = test_dao.create(data)

    assert result is not None


def test_create_missing_field(test_dao):
    data = {
        "lastName": "Ramos",
        "email": "ramos@example.com"
    }

    with pytest.raises(Exception):
        test_dao.create(data)

def test_create_wrong_type(test_dao):
    data = {
        "firstName": 123,
        "lastName": "Yamal",
        "email": "Yamal@example.com"
    }

    with pytest.raises(Exception):
        test_dao.create(data)

def test_create_duplicate_email(test_dao):
    data = {
        "firstName": "Arda",
        "lastName": "Guler",
        "email": "Yamal@example.com"
    }

    test_dao.create(data)

    with pytest.raises(Exception):
        test_dao.create(data)