import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Restaurant, Menu, MenuItem, Employee
from django.contrib.auth.models import User

@pytest.mark.django_db
@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
@pytest.fixture
def user():
    return User.objects.create_user(username='test_user', password='test_password')

@pytest.mark.django_db
@pytest.fixture
def restaurant(user):
    return Restaurant.objects.create(name='Test Restaurant', description='Test Description')

@pytest.mark.django_db
@pytest.fixture
def menu(restaurant):
    return Menu.objects.create(restaurant=restaurant, date='2024-05-15')

@pytest.mark.django_db
@pytest.fixture
def menu_item(menu):
    return MenuItem.objects.create(menu=menu, name='Test Item', price=10.99)

@pytest.mark.django_db
@pytest.fixture
def employee(user, restaurant):
    return Employee.objects.create(user=user, position='Waiter')

@pytest.mark.django_db
def test_authentication(api_client, user):
    response = api_client.post(reverse('token_obtain_pair'), {'username': 'test_user', 'password': 'test_password'}, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

    response = api_client.post(reverse('token_obtain_pair'), {'username': 'test_user', 'password': 'wrong_password'}, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_create_restaurant(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post(reverse('restaurant-list-create'), {'name': 'New Restaurant', 'description': 'New Description'}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.count() == 1

@pytest.mark.django_db
def test_upload_menu(api_client, user, restaurant):
    api_client.force_authenticate(user=user)
    response = api_client.post(reverse('menu-list-create'), {'restaurant': restaurant.id, 'date': '2024-05-15'}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Menu.objects.count() == 1

@pytest.mark.django_db
def test_create_employee(api_client, user, restaurant):
    api_client.force_authenticate(user=user)
    response = api_client.post(reverse('employee-list-create'), {'user': user.id, 'position': 'Waiter'}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.count() == 1

@pytest.mark.django_db
def test_get_current_day_menu(api_client, user, restaurant, menu):
    api_client.force_authenticate(user=user)
    response = api_client.get(reverse('current_day_menu_items') + f'?restaurant={restaurant.id}&date=2024-05-15', format='json')
    assert response.status_code == status.HTTP_200_OK

