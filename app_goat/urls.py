from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('list/', views.list, name='list'),
    path('list/<str:pk>/', views.detail, name='detail'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    path('diagnosis/result', views.result, name='result'),
   
   
    
    

]