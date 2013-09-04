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

from mercs.personnel.models import Person, Team
from mercs.gm.helpers import log
import random

def run_maintenance(force):
    """
    run repair/maintenance cycle for a force
    """
    log('Starting maintenance', force)

    vehicles = force.vehicle_set.all()

    teams = Team.objects.filter(person__force = force).distinct()

    for team in teams:
        team.remaining_maintenance = 480

    for vehicle in vehicles:
        assigned_teams = [team for team in teams
                          if team.vehicle == vehicle]

        if assigned_teams:
            team = assigned_teams[0]
            if team.remaining_maintenance >= vehicle.maintenance:
                _maintenance_with_team(team, vehicle, force)
            else:
                _maintenance_without_team(vehicle, force)
        else:
            _maintenance_without_team(vehicle, force)

    log('Maintenance done', force)

def _maintenance_with_team(team, vehicle, force):
    team.remaining_maintenance = team.remaining_maintenance - vehicle.maintenance
    skill_score = min([person.skill_set.filter(
                             skill_definition__skill_name = 'Technical')[0].skill_score
                       for person 
                       in team.person_set.all()])
    tn = skill_score

    roll = random.randint(1, 6) + random.randint(1, 6)

    if roll >= tn:
        log('Maintenance for vehicle {0} by team {1} succesful'.format(vehicle, team), force)
    else:
        log('Maintenance for vehicle {0} by team {1} failed'.format(vehicle, team), force)

def _maintenance_without_team(vehicle, force):
    tn = 10

    roll = random.randint(1, 6) + random.randint(1, 6)

    if roll >= tn:
        log('Maintenance for vehicle {0} without team succesful'.format(vehicle), force)
    else:
        log('Maintenance for vehicle {0} without team failed'.format(vehicle), force)

