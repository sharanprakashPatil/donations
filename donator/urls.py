from django.urls import path
from . import views

urlpatterns = [
    path('', views.donator_page, name='donator'),
]
