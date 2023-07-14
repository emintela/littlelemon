from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        extra_kwargs = {
            "price": {"min_value": 0},
            "inventory": {"min_value": 0},
        }
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        extra_kwargs = {
            "no_of_guests": {"min_value": 1},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name", "is_active", "is_staff", "groups", "url"]
        extra_kwargs = {
            "password": {"write_only": True},
            # "is_active": {"read_only": True},
        }