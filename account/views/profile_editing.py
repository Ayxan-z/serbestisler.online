from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfileEditingForm

@login_required(login_url='/')
def profile_editing(request):
    if request.method == 'POST':
        form = ProfileEditingForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, 'Profile updated')
            return redirect('homepage')
        
    else:
        form = ProfileEditingForm(instance=request.user)
    
    return render(request, 'pages/profile-editing.html', context={"form": form})

