from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'n_in_progress': projects.filter(state=2).count(),
        'n_paused': projects.filter(state=1).count(),
        'n_shipped': projects.filter(state=4).count(),
        'n_total': projects.count(),
    }
    return render(request, 'tracker/index.html', context)
