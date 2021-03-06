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
from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mercs.common.models import Parameter
from mercs.gm.models import GMLogEntry
from mercs.gm.cycle import run_cycle
from mercs.forces.models import Force
from mercs.integration.serializers import GMLogEntrySerializer, ForceSerializer

class CurrentDateView(APIView):

    def get(self, request, *args, **kw):

        current_date = Parameter.objects.get(parameter_name = 'current date').date_value   
        result = {'current_date': str(current_date.isoformat())}
        response = Response(result, status=status.HTTP_200_OK)
        return response

class ForceList(generics.ListAPIView):

    serializer_class = ForceSerializer

    def get_queryset(self):

        queryset = Force.objects.all()        

        return queryset

class ForceDetails(generics.ListAPIView):

    serializer_class = ForceSerializer

    def get_queryset(self):

        id = self.kwargs['id']
        queryset = Force.objects.all()
        queryset = queryset.filter(id = id)

        return queryset

class GMLogEntryList(generics.ListAPIView):
    
    serializer_class = GMLogEntrySerializer

    def get_queryset(self):

        queryset = GMLogEntry.objects.all()        
        date = self.request.QUERY_PARAMS.get('date', None)

        if date is not None:
            if date == 'current':
                current_date = Parameter.objects.get(parameter_name = 'current date').date_value
                queryset = queryset.filter(entry_date=current_date)
            else:
                queryset = queryset.filter(entry_date=date)

        return queryset

class GMLogEntryDetails(generics.ListAPIView):
    
    serializer_class = GMLogEntrySerializer

    def get_queryset(self):

        id = self.kwargs['id']
        queryset = GMLogEntry.objects.all()        
        queryset = queryset.filter(id = id)

        return queryset

@api_view(['POST'])
def cycle(request):
    if request.method == 'POST':
        days_to_advance = int(request.DATA['days'])

        param = Parameter.objects.filter(parameter_name = 'current date')[0]
        param.date_value = param.date_value + datetime.timedelta(1)
        param.save()
        current_date = param.date_value

        forces = Force.objects.all()

        for force in forces:
            run_cycle(force)

        return Response('', status=status.HTTP_200_OK)

