from django.shortcuts import render
from .models import HomeContent

def home_page(request):
    content = HomeContent.objects.first()
    # If no content exists yet, we'll fall back to defaults in the template
    return render(request, 'home.html', {'content': content})
