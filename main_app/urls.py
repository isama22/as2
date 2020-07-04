from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name="about"),
  path('contact', views.contact, name="contact"),

  path('accounts/signup/', views.signup, name='signup'),
  path('digitals/', views.digitals_index, name="digitals_index"),
  path('digitals/<int:digital_id>/', views.digitals_detail, name='digitals_detail'),
  path('digitals/create/', views.DigitalsCreate.as_view(), name='digitals_create'),
  path('digitals/<int:pk>/update/', views.DigitalUpdate.as_view(), name='digitals_update'),
  path('digitals/<int:pk>/delete/', views.DigitalDelete.as_view(), name='digitals_delete'),
  
]