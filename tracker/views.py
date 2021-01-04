from django.shortcuts import render
from .models import Project
from .states import id_for_string


def index(request):
    projects = Project.objects.all()

    filter_state = request.GET.get("filter", "all")
    filter_state_id = id_for_string(filter_state)

    filtered_projects = projects
    if filter_state_id > -1:
        filtered_projects = projects.filter(state=filter_state_id)

    context = {
        'projects': filtered_projects,
        'n_in_progress': projects.filter(state=2).count(),
        'n_paused': projects.filter(state=1).count(),
        'n_shipped': projects.filter(state=4).count(),
        'n_total': projects.count(),
    }

    return render(request, 'tracker/index.html', context)
