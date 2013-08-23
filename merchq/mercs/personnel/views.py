from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render

from mercs.personnel.models import Person
from mercs.forces.models import Force

def index(request):
    forces = Force.objects.all().annotate(personnel_count = Count('person'))
    context = {'forces': forces}

    return render(request, 'personnel/index.html', context)

def force_personnel(request, force_id):
    return HttpResponse("Hello, world. You're seeing a force")

def person_details(request, person_id):
	return HttpResponse("Hello, world. You're seeing a person")

