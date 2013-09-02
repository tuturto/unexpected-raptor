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
from mercs.forces.models import Force
from mercs.gm.cycle import run_cycle
from mercs.gm.models import GMLogEntry
from mercs.common.models import Parameter
import datetime

def index(request):

    context = {}

    return render(request, 'gm/index.html', context)

def gm_log(request):

    context = {}

    return render(request, 'gm/log.html', context)

def gm_cycle(request):

    param = Parameter.objects.filter(parameter_name = 'current date')[0]
    param.date_value = param.date_value + datetime.timedelta(1)
    param.save()

    forces = Force.objects.all()

    for force in forces:
        run_cycle(force)

    log = GMLogEntry.objects.filter(entry_date = param.date_value)

    context = {'year': param.date_value.year,
               'month': param.date_value.month,
               'day': param.date_value.day,
               'log': log}

    return render(request, 'gm/log.html', context)

