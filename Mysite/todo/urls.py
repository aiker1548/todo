from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]