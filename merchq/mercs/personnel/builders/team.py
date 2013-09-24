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

from mercs.personnel.models import Team
from mercs.personnel.builders.person import PersonBuilder
from mercs.astrography.builders import PlanetBuilder

class TeamBuilder(object):

    def __init__(self):
        super(TeamBuilder, self).__init__()

        self.team_name = 'generic team'
        self.vehicle = None
        self.remaining_maintenance = 480
        self.member_count = 7

        self.location = PlanetBuilder().build()

    def with_assigned_vehicle(self, vehicle):
        self.vehicle = vehicle
        return self

    def with_location(self, location):
        self.location = location
        return self

    def build(self):
        new_team = Team()
        new_team.team_name = self.team_name
        new_team.vehicle = self.vehicle
        new_team.remaining_maintenance = self.remaining_maintenance

        for i in xrange(self.member_count):
            member = (PersonBuilder(self)
                        .with_team(new_team)
                        .with_location(self.location)
                        .build())

        return new_team

    def build_and_save(self):
        new_team = self.build()
        new_team.save()
        return new_team

