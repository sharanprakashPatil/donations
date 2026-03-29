"""
URL configuration for donations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin as django_admin
from django.urls import path, include

from admin import views as admin_views

urlpatterns = [
    path('', include('home.urls')), # Serve the home page on the base route as requested
    path('admin/', django_admin.site.urls), # Default Django admin
    path('admin-login/', admin_views.admin_login, name='admin_login'), # Custom admin app
    path('admindata/', admin_views.admindata_page, name='admindata'), # Admin dashboard controlled by admin app
    path('verification/', include('verification.urls')), # Verification app
    path('user/', include('user.urls')), # User auth app
    path('base/', include('basepage.urls')), # Base landing page
    path('donator/', include('donator.urls')), # Donator functionality
    path('seeker/', include('seeker.urls')), # Seeker functionality
    path('userdata/', include('userdata.urls')), # User data metrics dashboard
]
