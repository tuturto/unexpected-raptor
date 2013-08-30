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

from django.db import models
from mercs.forces.models import Force

class QualityRating(models.Model):
    rating = models.CharField(max_length = 10)
    rating_name = models.CharField(max_length = 50)
    cost_modifier = models.FloatField(default = 1.0)
    
    def __unicode__(self):
        return 'rating {0} ({1})'.format(self.rating,
                                         self.rating_name)

class VehicleType(models.Model):
    type_name = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.type_name

class WeightClass(models.Model):
    weight_class = models.CharField(max_length = 50)
    vehicle_type = models.ForeignKey(VehicleType)
    lower_limit = models.IntegerField(default = 0)
    upper_limit = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return '{0} {1} ({2} - {3})'.format(self.weight_class,
                                            self.vehicle_type,
                                            self.lower_limit,
                                            self.upper_limit)

class SupportType(models.Model):
    support_name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.support_name

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length = 50)
    vehicle_type = models.ForeignKey(VehicleType)
    vehicle_weight = models.IntegerField(default = 0)

    maintenance = models.IntegerField(default = 0)
    
    support_type = models.ForeignKey(SupportType)
    owner = models.ForeignKey(Force,
                              blank = True,
                              null = True)
    base_price = models.IntegerField(default = 0)
    active = models.BooleanField(default = True)

    quality_rating = models.ForeignKey(QualityRating)

    def __unicode__(self):
        return '{0} ({1})'.format(self.vehicle_name,
                                  self.id)

