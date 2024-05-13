"""
URL configuration for app2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ObtainJWTView, RestaurantListCreateAPIView
from .views import MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView, MenuItemListCreateAPIView, \
    MenuItemRetrieveUpdateDestroyAPIView, EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView, \
    CurrentDayMenuAPIView, CurrentDayMenuItemAPIView

urlpatterns = [
    path('api/token/', ObtainJWTView.as_view(), name='token_obtain_pair'),
    path('api/restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('api/menu/', MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('api/menu/<int:pk>/', MenuRetrieveUpdateDestroyAPIView.as_view(), name='menu-retrieve-update-destroy'),
    path('api/menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list-create'),
    path('api/menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyAPIView.as_view(),
         name='menu-item-retrieve-update-destroy'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
    path('api/current_day_menu/', CurrentDayMenuAPIView.as_view(), name='current_day_menu'),
    path('api/current_day_menu_items/', CurrentDayMenuItemAPIView.as_view(), name='current_day_menu_items'),
]
