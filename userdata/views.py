from django.shortcuts import render, redirect

def userdata_page(request):
    if not request.session.get('is_user'):
        return redirect('/user/')
        
    # Passing placeholder metrics for the template to render
    context = {
        'donated_amount': 15500,
        'target_seeked_amount': 50000,
        'raised_amount': 12500,
    }
    return render(request, 'userdata.html', context)
