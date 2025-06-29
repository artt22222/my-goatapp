from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Diseases

# Create your views here.

def home(request): #เขียนอะไรใน () ก็เรียกใช้ตามนั้น
    return render(request,'app_goat/home.html')

def about(request):
    return render(request, 'app_goat/about.html')

def disease_list(request):
    diseases = Diseases.objects.all()
    context = {'diseases': diseases}
    return render(request, 'app_goat/disease_list.html',context)

def disease_detail(request, pk):
    disease = get_object_or_404(Diseases, pk=pk)
    context = {'disease': disease}
    return render(request, 'app_goat/disease_detail.html', context)



