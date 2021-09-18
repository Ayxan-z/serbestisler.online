from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_def(request):
    logout(request)
    
    return redirect('homepage') 

