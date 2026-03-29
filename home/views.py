from django.shortcuts import render
<<<<<<< HEAD
from .models import HomeContent

def home_page(request):
    content = HomeContent.objects.first()
    # If no content exists yet, we'll fall back to defaults in the template
    return render(request, 'home.html', {'content': content})
=======

def home_page(request):
    return render(request, 'home.html')
>>>>>>> 70875e671408b029b7d1f928a230940b9f2432a0
