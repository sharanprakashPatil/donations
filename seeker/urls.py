from django.urls import path
from . import views

urlpatterns = [
    path('', views.seeker_page, name='seeker'),
]
