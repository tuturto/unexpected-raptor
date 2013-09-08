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
from django.shortcuts import render, get_object_or_404
from mercs.astrography.models import StarSystem, Planet
from mercs.common.models import Parameter

def star_system(request, system_id):
    star_system = get_object_or_404(StarSystem, id = system_id)

    current_date = Parameter.objects.get(parameter_name = 'current date').date_value

    planets = star_system.planet_set.all()

    context = {'star_system': star_system,
               'planets': planets,
               'current_date': current_date}

    return render(request, 'astrography/star_system.html', context)

def planet(request, planet_id):
    planet = get_object_or_404(Planet, id = planet_id)

    current_date = Parameter.objects.get(parameter_name = 'current date').date_value

    context = {'star_system': planet.star_system,
               'planet': planet,
               'maintenance_modifiers': planet.maintenance_modifiers.all(),
               'current_date': current_date}

    return render(request, 'astrography/planet.html', context)

