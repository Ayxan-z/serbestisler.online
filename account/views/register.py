from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import RegisterForm
from django.contrib.auth import login, authenticate 

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, 'Sistemə giriş edildi')
            return redirect('homepage')
            
    else:
        form = RegisterForm()
    
    return render(request, 'pages/register.html', context={"form": form})
