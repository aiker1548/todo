from django.urls import path
from django.urls import include
from .views import home_view

urlpatterns = [
    path('', home_view)
]