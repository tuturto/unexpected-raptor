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

from mercs.armoury.models import VehicleType, Vehicle

class VehicleTypeBuilder(object):

    def __init__(self):
        super(VehicleTypeBuilder, self).__init__()

        self.type_name = 'generic vehicle'

    def with_name(self, type_name):
        self.type_name = type_name
        return self

    def build(self):
        new_type = VehicleType()
        new_type.type_name = self.type_name

        return new_type

    def build_and_save(self):
        new_type = self.build()
        new_type.save()

        return new_type

class VehicleBuilder(object):

    def __init__(self):
        super(VehicleBuilder, self).__init__()

        self.vehicle_name = 'random vehicle'
        self.vehicle_type = VehicleTypeBuilder().build()
        self.vehicle_weight = 50

        self.maintenance = 30
    
        self.support_type = SupportTypeBuilder().build()
        self.owner = ForceBuilder().build()
        self.base_price = 5000000
        self.active = True

        self.quality_rating = QualityRatingBuilder().build()
        self.location = PlanetBuilder().build()

    def build(self):
        new_vehicle = Vehicle()
        new_vehicle.vehicle_name = self.vehicle_name
        new_vehicle.vehicle_type = self.vehicle_type
        new_vehicle.vehicle_weight = self.vehicle_weight
        new_vehicle.maintenance = self.maintenance
        new_vehicle.support_type = self.support_type
        new_vehicle.owner = self.owner
        new_vehicle.base_price = self.base_price
        new_vehicle.active = self.active
        new_vehicle.quality_rating = self.quality_rating
        new_vehicle.location = self.location

        return new_vehicle

    def build_and_save(self):
        new_vehicle = self.build()
        new_vehicle.save()
        return new_vehicle

