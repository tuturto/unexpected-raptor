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

from rest_framework import serializers
from mercs.gm.models import GMLogEntry
from mercs.forces.models import Force

class ForceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Force
        fields = ('id', 'force_name')

class GMLogEntrySerializer(serializers.ModelSerializer):

    force = serializers.HyperlinkedRelatedField(many=False, 
                                                read_only=True,
                                                view_name='mercs.integration.forces')

    class Meta:
        model = GMLogEntry
        fields = ('id', 'entry_date', 'text', 'force')

