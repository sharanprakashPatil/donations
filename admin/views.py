from django.shortcuts import render, redirect

def admin_login(request):
    if request.method == 'POST':
        # Provide backend fallback for the login credentials
        admin_id = request.POST.get('adminId')
        password = request.POST.get('password')
        
        if admin_id == '9483870558' and password in ['onlyfriends2025', 'only friends2025']:
            # Set a session object granting admin access
            request.session['is_admin'] = True
            return redirect('/admindata/')
        else:
            return render(request, 'admin.html', {'error': 'Invalid credentials'})
    return render(request, 'admin.html')

def admindata_page(request):
    # Secure the dashboard by checking the session token created upon admin login
    if not request.session.get('is_admin'):
        return redirect('/admin-login/')
    return render(request, 'admindata.html')


