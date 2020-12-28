from django.shortcuts import render
from .models import Project


def index(request):
    return render(request, 'tracker/index.html')
