import requests

USER_URL = "http://127.0.0.1:5001"
PRODUCT_URL = "http://127.0.0.1:5002"


def test_user_health():
    response = requests.get(
        f"{USER_URL}/health", timeout=5
    )
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_users():
    response = requests.get(
        f"{USER_URL}/users", timeout=5
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_product_health():
    response = requests.get(
        f"{PRODUCT_URL}/health", timeout=5
    )
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_products():
    response = requests.get(
        f"{PRODUCT_URL}/products", timeout=5
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
