import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Kitten, Breed
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def token(user):
    response = APIClient().post(reverse('token_obtain_pair'), {
        'username': 'testuser',
        'password': 'testpass'
    })
    return response.data['access']


@pytest.fixture
def breed():
    return Breed.objects.create(name='Мейн-кун')


@pytest.fixture
def kitten(breed, user):
    return Kitten.objects.create(breed=breed, color='белый', age_in_months=6, description='Милый котёнок', owner=user)


@pytest.mark.django_db
def test_get_all_kittens(api_client, token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.get(reverse('kitten-list'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_kitten(api_client, token, breed):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    data = {
        'breed': breed.id,
        'color': 'чёрный',
        'age_in_months': 5,
        'description': 'Милый чёрный котёнок'
    }
    response = api_client.post(reverse('kitten-create'), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Kitten.objects.count() == 1


@pytest.mark.django_db
def test_update_kitten(api_client, token, kitten):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    data = {
        'color': 'серый',
        'age_in_months': 7,
        'description': 'Обновлённый котёнок',
        'breed': kitten.breed.id  # Передаем ID породы вместо строки
    }
    response = api_client.put(reverse('kitten-detail', args=[kitten.id]), data, format='json')
    assert response.status_code == status.HTTP_200_OK





@pytest.mark.django_db
def test_delete_kitten(api_client, token, kitten):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.delete(reverse('kitten-detail', args=[kitten.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Kitten.objects.count() == 0


@pytest.mark.django_db
def test_get_kitten_detail(api_client, token, kitten):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.get(reverse('kitten-detail', args=[kitten.id]))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['color'] == kitten.color
    assert response.data['age_in_months'] == kitten.age_in_months
