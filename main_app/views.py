from django.shortcuts import render, redirect
from .models import Fiber, Figurative, Digital, FiberPhoto, FigurativePhoto, DigitalPhoto
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')  


def digitals_index(request):
  digitals = Digital.objects.all()
  return render(request, 'digitals/index.html', { 'digitals': digitals })

def digitals_detail(request, digital_id):
  digital = Digital.objects.get(id=digital_id)
  return render(request, 'digitals/detail.html', { 'digital': digital }) 

class DigitalsCreate(LoginRequiredMixin, CreateView):
  model = Digital
  fields = '__all__'
  success_url = '/digitals/'    

class DigitalUpdate(LoginRequiredMixin, UpdateView):
  model = Digital
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  success_url = '/digitals/'

class DigitalDelete(LoginRequiredMixin, DeleteView):
  model = Digital
  success_url = '/digitals/'  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)