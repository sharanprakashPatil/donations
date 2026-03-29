from django.urls import path
from . import views

urlpatterns = [
    # Map the root url of admindata app to the dashboard view
    path('', views.admindata_page, name='admindata'),
]
