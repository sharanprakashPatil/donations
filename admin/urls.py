from django.urls import path
from . import views

urlpatterns = [
    # Creating a custom path for our admin page
    path('', views.admin_login, name='admin_login'),
]
