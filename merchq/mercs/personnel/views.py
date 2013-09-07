# -*- coding: utf-8 -*-

#   Copyright 2013 Tuukka Turto
#
#   This file is part of unexpected-raptor.
#
#   unexpected-raptor is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   unexpected-raptor is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with unexpected-raptor.  If not, see <http://www.gnu.org/licenses/>.

from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from mercs.personnel.models import Person, Position
from mercs.forces.models import Force
from mercs.common.models import Parameter

def index(request):
    forces = Force.objects.all().annotate(personnel_count = Count('person'))
    current_date = Parameter.objects.filter(parameter_name = 'current date')[0].date_value

    context = {'forces': forces,
               'current_date': current_date}

    return render(request, 'personnel/index.html', context)

def force_personnel(request, force_id):
    force = get_object_or_404(Force, id=force_id)
    people = force.person_set.all().order_by('position', 'person_name')
    positions = Position.objects.all().order_by('position_name')
    total_salary = sum([person.get_salary() for person
                        in people])

    pos_data = []

    for position in positions:
        matching_people = [person for person in people
                           if person.position == position]
        pos_data.append([position,
                         matching_people,
                         sum([person.get_salary() for person
                              in matching_people])])
   
    current_date = Parameter.objects.filter(parameter_name = 'current date')[0].date_value

    context = {'force': force,
               'force_personnel': pos_data,
               'total_salary': total_salary,
               'current_date': current_date}

    return render(request, 'personnel/force_personnel.html', context)

def person_details(request, person_id):

    person = get_object_or_404(Person, id=person_id)
    current_date = Parameter.objects.filter(parameter_name = 'current date')[0].date_value

    context = {'person': person,
               'force': person.force,
               'current_date': current_date}

    return render(request, 'personnel/person_details.html', context)

