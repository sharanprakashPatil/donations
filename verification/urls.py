from django.urls import path
from . import views

urlpatterns = [
    # Map the root url of verification app to the dashboard view
    path('', views.verification_page, name='verification'),
]
