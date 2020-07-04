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
  path('digitals/<int:digital_id>/digital_photo/', views.digital_photo, name='digital_photo'),
  path('digitals/<int:digital_id>/delete_digital_photo/', views.delete_digital_photo, name='delete_digital_photo'),

  path('figuratives/', views.figuratives_index, name="figuratives_index"),
  path('figuratives/<int:figurative_id>/', views.figuratives_detail, name='figuratives_detail'),
  path('figuratives/create/', views.FigurativesCreate.as_view(), name='figuratives_create'),
  path('figuratives/<int:pk>/update/', views.FigurativeUpdate.as_view(), name='figuratives_update'),
  path('figuratives/<int:pk>/delete/', views.FigurativeDelete.as_view(), name='figuratives_delete'),
  path('figuratives/<int:figurative_id>/figurative_photo/', views.figurative_photo, name='figurative_photo'),
  path('figuratives/<int:figurative_id>/delete_figurative_photo/', views.delete_figurative_photo, name='delete_figurative_photo'),
  
]