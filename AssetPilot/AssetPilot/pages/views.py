from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def contact_view(request):
    return render(request, 'pages/contact.html')