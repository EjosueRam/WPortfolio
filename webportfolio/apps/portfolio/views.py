from django.shortcuts import render
from .models import Portfolio

def home(request):
    projects = Portfolio.objects.all()
    return render(request, 'home.html', {'projects' : projects})
