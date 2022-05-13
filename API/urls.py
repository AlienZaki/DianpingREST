from django.urls import path
from .views import index, get_hotel_details


urlpatterns = [
    path('', index),
    path('hotel/', get_hotel_details),
]