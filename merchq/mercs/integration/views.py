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
import datetime
import json
from rest_framework import mixins
from rest_framework import generics

from mercs.common.models import Parameter
from mercs.gm.models import GMLogEntry
from mercs.integration.serializers import GMLogEntrySerializer

def current_date(request):

    current_date = Parameter.objects.get(parameter_name = 'current date').date_value   

    response_data = {}
    response_data['current_date'] = str(current_date.isoformat())
   
    return HttpResponse(json.dumps(response_data), content_type="application/json")


class GMLogEntryList(generics.ListAPIView):
    
    serializer_class = GMLogEntrySerializer

    def get_queryset(self):

        queryset = GMLogEntry.objects.all()        
        date = self.request.QUERY_PARAMS.get('date', None)

        if date is not None:
            queryset = queryset.filter(entry_date=date)

        return queryset

