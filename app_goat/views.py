from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Diseases,GoatStatistics

# Create your views here.



def about(request):
    return render(request, 'app_goat/about.html')

def form(request):
    return render(request, 'app_goat/form.html')

def list(request):
    diseases = Diseases.objects.all()
    context = {'diseases': diseases}
    return render(request, 'app_goat/list.html',context)

def detail(request, pk):
    disease = get_object_or_404(Diseases, pk=pk)
    context = {'disease': disease}
    return render(request, 'app_goat/detail.html', context)

def home(request):
    stats = GoatStatistics.objects.last()  # ใช้ล่าสุด
    return render(request, 'app_goat/home.html', {'stats': stats})

