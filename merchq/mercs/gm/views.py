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
import json

def index(request):

    current_date = Parameter.objects.filter(parameter_name = 'current date')[0].date_value

    context = {'current_date': current_date}

    return render(request, 'gm/index.html', context)

def gm_log(request, year = None, month = None, day = None):

    current_date = Parameter.objects.get(parameter_name = 'current date').date_value   

    if year:
        shown_date = datetime.date(year = int(year),
                                   month = int(month),
                                   day = int(day))
    else:
        shown_date = current_date

    yesterday = shown_date - datetime.timedelta(1)
    tomorrow = shown_date + datetime.timedelta(1)

    log = GMLogEntry.objects.filter(entry_date = shown_date)

    context = {'current_date': current_date,
               'shown_date': shown_date,
               'yesterday': yesterday,
               'tomorrow': tomorrow,
               'log': log}

    return render(request, 'gm/log.html', context)

def gm_cycle(request):

    param = Parameter.objects.filter(parameter_name = 'current date')[0]
    param.date_value = param.date_value + datetime.timedelta(1)
    param.save()
    current_date = param.date_value

    forces = Force.objects.all()

    for force in forces:
        run_cycle(force)

    log = GMLogEntry.objects.filter(entry_date = param.date_value)

    yesterday = current_date - datetime.timedelta(1)
    tomorrow = current_date + datetime.timedelta(1)

    context = {'year': param.date_value.year,
               'month': param.date_value.month,
               'day': param.date_value.day,
               'log': log,
               'current_date': current_date,
               'yesterday': yesterday,
               'tomorrow': tomorrow,}

    return render(request, 'gm/log.html', context)

def log_entries(request, year = None, month = None, day = None):

    current_date = Parameter.objects.get(parameter_name = 'current date').date_value   

    if year:
        shown_date = datetime.date(year = int(year),
                                   month = int(month),
                                   day = int(day))
    else:
        shown_date = current_date

    log = GMLogEntry.objects.filter(entry_date = shown_date)

    response_data = {}
    response_data['entries'] = []

    for log_entry in log:  
        entry = {}
        entry['entry_date'] = str(log_entry.entry_date)
        entry['text'] = str(log_entry.text)
        response_data['entries'].append(entry)
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

