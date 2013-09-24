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

from mercs.astrography.models import Planet, StarSystem, Faction

class FactionBuilder(object):

    def __init__(self):
        super(FactionBuilder, self).__init__()

        self.name = 'generic faction'

    def build(self):
        new_faction = Faction()
        new_faction.name = self.name

        return new_faction

    def build_and_save(self):
        new_faction = self.build()
        new_faction.save()
        return new_faction

class StarSystemBuilder(object):

    def __init__(self):
        super(StarSystemBuilder, self).__init__()

        self.name = 'generic star system'
        self.location = (0, 0)
        self.faction = FactionBuilder().build()

    def build(self):
        new_system = StarSystem()
        new_system.name = self.name
        new_system.location_x = self.location[0]
        new_system.location_y = self.location[1]
        new_system.faction = self.faction

        return new_system

    def build_and_save(self):
        new_system = self.build()
        new_system.faction.save()
        new_system.save()
        return new_system

class PlanetBuilder(object):

    def __init__(self):
        super(PlanetBuilder, self).__init__()

        self.name = 'generic planet'
        self.system_position = 1
        self.star_system = StarSystemBuilder().build()
        self.gravity = 1
        self.maintenance_modifiers = []

    def build(self):
        new_planet = Planet()
        new_planet.name = self.name
        new_planet.system_position = self.system_position
        new_planet.star_system = self.star_system
        new_planet.gravity = self.gravity

        return new_planet

    def build_and_save(self):
        new_planet = self.build()
        new_planet.save()

        return new_planet

