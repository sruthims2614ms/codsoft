from django.urls import path
from .views import generated

urlpatterns = [
    path('', generated, name='generate_password'),
]
