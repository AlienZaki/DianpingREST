from django.urls import path
from .views import index, get_hotel_details


urlpatterns = [
    path('', index),
    path('api/v1/hotel/', get_hotel_details),
]