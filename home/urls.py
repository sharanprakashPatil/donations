from django.urls import path
from . import views

urlpatterns = [
    # Map the root url of this app to our home_page view
    path('', views.home_page, name='home'),
]
