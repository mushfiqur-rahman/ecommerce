import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):
        # A: Arrange

        # A: Act
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_admin_returns_403(self):
        # A: Arrange

        # A: Act
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_invalid_returns_400(self):
        # A: Arrange

        # A: Act
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': ''})

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_user_is_valid_returns_201(self):
        # A: Arrange

        # A: Act
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
