from django.shortcuts import render, redirect

def base_page(request):
    # Optional backend check: ensure only people who clicked login can access the dashboard.
    if not request.session.get('is_user'):
        return redirect('/user/')
    return render(request, 'base.html')
