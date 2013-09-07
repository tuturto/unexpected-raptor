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
from mercs.armoury.models import MaintenanceModifier

class Faction(models.Model):

    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class StarSystem(models.Model):

    name = models.CharField(max_length = 100)
    location_x = models.FloatField(default = 0)
    location_y = models.FloatField(default = 0)
    faction = models.ForeignKey(Faction)

    def __unicode__(self):
        return self.name

class Star(models.Model):

    name = models.CharField(max_length = 100)
    spectral_class = models.CharField(max_length = 10)
    star_system = models.ForeignKey(StarSystem)

    def __unicode__(self):
        return self.name

class Planet(models.Model):

    name = models.CharField(max_length = 100)
    system_position = models.IntegerField(default = 0)
    star_system = models.ForeignKey(StarSystem)
    gravity = models.FloatField(default = 0.0)
    maintenance_modifiers = models.ManyToManyField(MaintenanceModifier)

    def __unicode__(self):
        return self.name

