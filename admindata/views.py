from django.shortcuts import render, redirect

def admindata_page(request):
    # Secure the dashboard by checking the session token created upon login
    if not request.session.get('is_admin'):
        return redirect('/admin-login/')
    return render(request, 'admindata.html')
