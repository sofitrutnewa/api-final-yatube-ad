import pytest

@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser', password='1234567'
    )

@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser2', password='1234567'
    )

@pytest.fixture
def another_user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUserAnother', password='1234567'
    )

@pytest.fixture
def token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)
    token_data = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    print(f"=== TOKEN created for user {user.username}: {token_data['access'][:50]}...")
    return token_data

@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    print(f"=== CLIENT credentials set with token: Bearer {token['access'][:50]}...")
    return client
