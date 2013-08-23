from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render

from mercs.personnel.models import Person, Position
from mercs.forces.models import Force

def index(request):
    forces = Force.objects.all().annotate(personnel_count = Count('person'))
    context = {'forces': forces}

    return render(request, 'personnel/index.html', context)

def force_personnel(request, force_id):
    force = Force.objects.get(id=force_id)
    people = force.person_set.all().order_by('position')
    positions = Position.objects.all().order_by('position_name')

    pos_data = []

    for position in positions:
        matching_people = [person for person in people
                           if person.position == position]
        pos_data.append([position, matching_people])
   
    context = {'force': force,
               'force_personnel': pos_data}

    return render(request, 'personnel/force_personnel.html', context)

def person_details(request, person_id):
	return HttpResponse("Hello, world. You're seeing a person")

