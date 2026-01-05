from django.urls import path
from .views import radio_view

urlpatterns = [
    path('', radio_view, name='radio_view'),
]
