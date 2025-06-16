import requests
import pytest

# ✅ Basic GET request test


def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    print("✅ test_get_users passed")

# ✅ Check a specific field in first user


def test_first_user_has_email():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert "email" in data[0]
    assert "@" in data[0]["email"]
    print("✅ test_first_user_has_email passed")

# ✅ Negative test: invalid endpoint


def test_invalid_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/invalid123")
    assert response.status_code == 404
    print("✅ test_invalid_endpoint passed")
