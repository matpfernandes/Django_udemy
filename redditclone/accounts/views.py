from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def singup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken' })
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password didn\'t match' })
    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if request.POST['next'] is not None:
                return redirect(request.POST['next'])
            login(request, user)
            return render(request, 'accounts/login.html', {'error':'Logins successful!' })
        else:
            return render(request, 'accounts/login.html', {'error':'The Username and Password didn\'t match' })
    else:
        return render(request, 'accounts/login.html')