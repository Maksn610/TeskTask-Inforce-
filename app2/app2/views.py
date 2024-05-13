from datetime import date
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Employee, Menu, MenuItem, Restaurant
from .serializers import EmployeeSerializer, MenuItemSerializer, MenuSerializer, RestaurantSerializer


class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CurrentDayMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        current_date = date.today()
        return Menu.objects.filter(date=current_date)


class CurrentDayMenuItemAPIView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        current_date = date.today()
        return MenuItem.objects.filter(menu__date=current_date)
