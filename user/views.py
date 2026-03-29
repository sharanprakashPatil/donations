from django.shortcuts import render, redirect

def user_auth_page(request):
    if request.method == 'POST':
        # Simulated authentication/registration logic for any user form sumitted
        request.session['is_user'] = True
        return redirect('/userdata/')
            
    return render(request, 'user.html')
