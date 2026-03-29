from django.urls import path
from . import views

urlpatterns = [
    # Map the root url of user app to the signin/signup view
    path('', views.user_auth_page, name='user_auth'),
]
