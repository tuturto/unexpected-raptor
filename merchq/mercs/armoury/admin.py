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

from django.contrib import admin

from mercs.armoury.models import VehicleType, WeightClass, SupportType
from mercs.armoury.models import Vehicle, QualityRating, MaintenanceModifier
from mercs.armoury.models import TechRating, Equipment, Availability

admin.site.register(VehicleType)
admin.site.register(WeightClass)
admin.site.register(SupportType)
admin.site.register(Vehicle)
admin.site.register(QualityRating)
admin.site.register(MaintenanceModifier)
admin.site.register(TechRating)
admin.site.register(Equipment)
admin.site.register(Availability)

