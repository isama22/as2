from django.shortcuts import render, redirect
from .models import Fiber, Figurative, Digital, FiberPhoto, FigurativePhoto, DigitalPhoto
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')  

