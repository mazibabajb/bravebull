from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "brave/index.html")

def contact(request):
    return render(request, "brave/contact.html")

def about(request):
    return render(request, "brave/about.html")        

def courses(request):
    return render(request, "brave/index.html")

def services(request):
    return render(request, "brave/index.html")    
