import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Restaurant, Menu, MenuItem, Employee
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='test_user', password='test_password')

@pytest.fixture
def restaurant(user):
    return Restaurant.objects.create(owner=user, name='Test Restaurant', description='Test Description')

@pytest.fixture
def menu(restaurant):
    return Menu.objects.create(restaurant=restaurant, date='2024-05-15')

@pytest.fixture
def menu_item(menu):
    return MenuItem.objects.create(menu=menu, name='Test Item', price=10.99)

@pytest.fixture
def employee(user, restaurant):
    return Employee.objects.create(user=user, restaurant=restaurant, position='Waiter')

def test_authentication(api_client, user):
    response = api_client.post(reverse('token_obtain_pair'), {'username': 'test_user', 'password': 'test_password'}, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

    response = api_client.post(reverse('token_obtain_pair'), {'username': 'test_user', 'password': 'wrong_password'}, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_create_restaurant(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post(reverse('restaurant-list'), {'name': 'New Restaurant', 'description': 'New Description'}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.count() == 1

def test_upload_menu(api_client, user, restaurant):
    api_client.force_authenticate(user=user)
    response = api_client.post(reverse('menu-list'), {'restaurant': restaurant.id, 'date': '2024-05-15'}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Menu.objects.count() == 1

def test_create_employee(api_client, user, restaurant):
    api_client.force_authenticate(user=user)
    response = api_client.post(reverse('employee-list'), {'user': user.id, 'restaurant': restaurant.id, 'position': 'Waiter'}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.count() == 1

def test_get_current_day_menu(api_client, user, restaurant, menu):
    api_client.force_authenticate(user=user)
    response = api_client.get(reverse('menu-list') + f'?restaurant={restaurant.id}&date=2024-05-15', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'results' in response.data

def test_get_results_for_current_day(api_client, user, restaurant):
    api_client.force_authenticate(user=user)
    response = api_client.get(reverse('results-list') + f'?restaurant={restaurant.id}&date=2024-05-15', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'results' in response.data
