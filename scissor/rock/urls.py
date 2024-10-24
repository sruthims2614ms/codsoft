from django.urls import path
from .views import games, reset

urlpatterns = [
    path('', games, name='games'),
    path('reset/', reset, name='reset'),
]
