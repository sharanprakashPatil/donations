from django.urls import path
from . import views

urlpatterns = [
    # Map the root url of basepage app to the base view
    path('', views.base_page, name='base'),
]
