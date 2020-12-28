from django.shortcuts import render
from .models import Project


def index(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'tracker/index.html', context)
