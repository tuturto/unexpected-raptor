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
from mercs.common.models import Parameter
import datetime
import json

def current_date(request):

    current_date = Parameter.objects.get(parameter_name = 'current date').date_value   


    response_data = {}
    response_data['current_date'] = str(current_date.isoformat())
   
    return HttpResponse(json.dumps(response_data), content_type="application/json")

