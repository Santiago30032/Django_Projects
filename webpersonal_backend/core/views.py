from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request): 
    return render(request, "core/home.html") #Lllamado de template, SE DEBE AGREGAR LA APP AL INSTALLED APPS EN EL settings.py
def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")