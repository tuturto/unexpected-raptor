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

from mercs.armoury.models import MaintenanceCheck
from mercs.personnel.models import Person, Team
from mercs.common.models import Parameter
from mercs.gm.helpers import log
import random

def run_maintenance(force):
    """
    run repair/maintenance cycle for a force
    """
    log('Starting maintenance', force)

    vehicles = force.vehicle_set.all()
    teams = Team.objects.filter(person__force = force).distinct()

    maintained_vehicles = []

    for team in teams:
        team.remaining_maintenance = 480

    team, vehicle = get_maintenance_unit(force, maintained_vehicles)
    while vehicle:
        do_maintenance(team, vehicle)
        team, vehicle = get_maintenance_unit(force, maintained_vehicles)

    log('Maintenance done', force)

def get_maintenance_unit(force, maintained_vehicles):
    """
    Get vehicle and team to do a maintenance on it
    If there is no dedicated team or a free team, no team is assigned
    In that case the team is None
    In case there is no maintenance to be done, vehicle is None
    """
    return None, None

def modifiers(team, vehicle, force):
    """
    Get sum of modifiers that might affect to maintenance
    """
    mods = vehicle.location.maintenance_modifiers.all()
    total_modifier = sum([modifier.modifier for modifier in mods])
    for modifier in mods:
        log('modifier {0}: {1}'.format(modifier.name, modifier.modifier), force)

    return total_modifier

