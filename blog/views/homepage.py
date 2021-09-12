from django.shortcuts import render

def homePage(request):
    return render(request, 'pages/homepage.html', context={})

