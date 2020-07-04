from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Fiber(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return self.title

    def get_absolute_url(self):
     return reverse('detail', kwargs={'fiber_id': self.id}) 

class Figurative(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return self.title     

     #in python shell f.save() if for fibers and fg.save() is for figurative
    def get_absolute_url(self):
     return reverse('detail', kwargs={'figurative_id': self.id})

class Digital(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return self.title 

    def get_absolute_url(self):
     return reverse('detail', kwargs={'digital_id': self.id})

class FiberPhoto(models.Model):
    url = models.CharField(max_length=200)
    fiber = models.ForeignKey(Fiber, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for fiber_id: {self.fiber_id} @{self.url}" 

class FigurativePhoto(models.Model):
    url = models.CharField(max_length=200)
    figurative = models.ForeignKey(Figurative, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for figurative_id: {self.figurative_id} @{self.url}" 

class DigitalPhoto(models.Model):
    url = models.CharField(max_length=200)
    digital = models.ForeignKey(Digital, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for digital_id: {self.digital_id} @{self.url}"         