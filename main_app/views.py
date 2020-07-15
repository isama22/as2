from django.shortcuts import render, redirect
from .models import Fiber, Figurative, Digital, FiberPhoto, FigurativePhoto, DigitalPhoto
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'isaartsite'

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

def digital_photo(request, digital_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo =DigitalPhoto(url=url, digital_id=digital_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('digitals_detail', digital_id=digital_id)  

def delete_digital_photo(request, digital_id):
    # key = DigitalPhoto.objects.get(digital_id=digital_id)
    key = DigitalPhoto.objects.last()
    key.delete()
    return redirect('digitals_detail', digital_id=digital_id)    

def figuratives_index(request):
  figuratives = Figurative.objects.all()
  return render(request, 'figuratives/index.html', { 'figuratives': figuratives })

def figuratives_detail(request, figurative_id):
  figurative = Figurative.objects.get(id=figurative_id)
  return render(request, 'figuratives/detail.html', { 'figurative': figurative }) 

class FigurativesCreate(LoginRequiredMixin, CreateView):
  model = Figurative
  fields = '__all__'
  success_url = '/figuratives/'

class FigurativeUpdate(LoginRequiredMixin, UpdateView):
  model = Figurative
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  success_url = '/figuratives/'

class FigurativeDelete(LoginRequiredMixin, DeleteView):
  model = Figurative
  success_url = '/figuratives/'

def figurative_photo(request, figurative_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo =FigurativePhoto(url=url, figurative_id=figurative_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('figuratives_detail', figurative_id=figurative_id)  


def delete_figurative_photo(request, figurative_id):
    #.all() deletes all photos if two images were uploaded on accident while loading, but deletes ALL fig photos
    key = FigurativePhoto.objects.last()
    key.delete()
    
    return redirect('figuratives_detail', figurative_id=figurative_id)


def fibers_index(request):
  fibers = Fiber.objects.all()
  return render(request, 'fibers/index.html', { 'fibers': fibers })

def fibers_detail(request, fiber_id):
  fiber = Fiber.objects.get(id=fiber_id)
  return render(request, 'fibers/detail.html', { 'fiber': fiber })  

class FibersCreate(LoginRequiredMixin, CreateView):
  model = Fiber
  fields = '__all__'
  success_url = '/fibers/'
  # def form_valid(self, form):
  #   form.instance.user = self.request.user
  #   return super().form_valid(form)

class FiberUpdate(LoginRequiredMixin, UpdateView):
  model = Fiber
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  success_url = '/fibers/'

class FiberDelete(LoginRequiredMixin, DeleteView):
  model = Fiber
  success_url = '/fibers/'

def fiber_photo(request, fiber_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo =FiberPhoto(url=url, fiber_id=fiber_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('fibers_detail', fiber_id=fiber_id)  


def delete_fiber_photo(request, fiber_id):
    key = FiberPhoto.objects.last()
    key.delete()
    
    return redirect('fibers_detail', fiber_id=fiber_id)    


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