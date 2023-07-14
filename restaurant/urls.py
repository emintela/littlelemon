from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = DefaultRouter(trailing_slash=False)
router.register("users", views.UserViewSet, basename="user")
router.register("menu-items", views.MenuViewSet, basename="menu-items")
router.register("bookings", views.BookingViewSet, basename="bookings")


urlpatterns = [
    path('', views.index, name="index"),
    #path("", include(router.urls)),
    path("home/", views.index, name="index"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", obtain_auth_token),  
]