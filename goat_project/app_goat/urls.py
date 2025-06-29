from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('diseases/', views.disease_list, name='disease_list'),
    path('diseases/<int:pk>/', views.disease_detail, name='disease_detail'),
    #path('diagnosis/',views.diagnosis_form, name='diagnosis_form'),
    #path('diagnosis/result/',views.diagnosis_result, name='diagnosis_result'),
   
    
    

]