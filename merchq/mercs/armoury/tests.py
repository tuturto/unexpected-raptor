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

from mercs.armoury.maintenance import *
from mercs.armoury.models import *
from mercs.personnel.models import *
from mercs.armoury.builders import *
from mercs.personnel.builders import *

import unittest

class MaintenanceTests(unittest.TestCase):

    def test_get_assigned_maintenance_team(self):
        """
        the dedicated maintenance team is always preferred
        """
        type_vehicle = (VehicleTypeBuilder()
                            .build_and_save())

        merc_force = (ForceBuilder()
                            .build_and_save())

        secret_base = (PlanetBuilder()
                            .build_and_save())

        vehicle = (VehicleBuilder()
                    .with_type(type_vehicle)
                    .with_maintenance(30)
                    .with_owner(merc_force)
                    .with_location(secret_base)
                    .build_and_save())

        vehicles = [vehicle]

        maintenance_team = (TeamBuilder()
                                .with_assigned_vehicle(vehicle)
                                .with_skills_for(vehicle)
                                .build_and_save())
        random_team = (TeamBuilder()
                            .with_skills_for(vehicle)
                            .build_and_save())

        teams = [random_team,
                 maintenance_team]
        maintained_vehicles = []

        team, vehicle = get_maintenance_unit(vehicles, teams, maintained_vehicles)

        assert team == maintenance_team

