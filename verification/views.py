from django.shortcuts import render, redirect

def verification_page(request):
    # Secure the endpoint to ensure only admins can process these documents
    if not request.session.get('is_admin'):
        return redirect('/admin-login/')
    return render(request, 'verification.html')
