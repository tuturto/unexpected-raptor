from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from mercs.forces.models import Force

def index(request):
    forces = Force.objects.all()

    context = {}

    return render(request, 'finances/index.html', context)

def force_finances(request, force_id):
    forces = Force.objects.all()

    context = {}

    return render(request, 'finances/force_finances.html', context)

