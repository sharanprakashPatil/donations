from django.urls import path
from . import views

urlpatterns = [
    # Map the root url of userdata app to the dashboard view
    path('', views.userdata_page, name='userdata'),
]
