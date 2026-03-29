from django.shortcuts import render, redirect

def seeker_page(request):
    if not request.session.get('is_user'):
        return redirect('/user/')
    # Currently pointing to a dummy placeholder template until user builds it out
    return render(request, 'seeker.html')
