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

    _maintenance_result(team, vehicle, force, roll, tn)
       

def _maintenance_without_team(vehicle, force):
    param = Parameter.objects.get(parameter_name = 'no team maintenance')
    tn = param.integer_value

    roll = random.randint(1, 6) + random.randint(1, 6)

    _maintenance_result(None, vehicle, force, roll, tn)
        

def _maintenance_result(team, vehicle, force, roll, target_number):
    margin = roll - target_number

    if margin < 0:
        if team:
            log('Maintenance for vehicle {0} by team {1} failed with margin {2}'.format(vehicle, 
                                                                                        team,
                                                                                        margin), force)
        else:
            log('Maintenance for vehicle {0} without team failed with margin {1}'.format(vehicle,
                                                                                         margin), force)
    else:
        if team:
            log('Maintenance for vehicle {0} by team {1} succesful with margin {2}'.format(vehicle,
                                                                                           team,
                                                                                           margin), force)
        else:
            log('Maintenance for vehicle {0} without team succesful with margin {1}'.format(vehicle,
                                                                                            margin), force)

    _maintenance_check(team, vehicle, force, margin)

def _maintenance_check(team, vehicle, force, margin):
    checks = MaintenanceCheck.objects.filter(margin = margin,
                                             quality_rating = vehicle.quality_rating)

    if checks:
        check = checks[0]
    
        _report_change_in_quality_rating(vehicle, check)
        vehicle.quality_rating = check.new_quality_rating

        vehicle.save()
    else:
        if margin < 0:
            checks = MaintenanceCheck.objects.filter(quality_rating = vehicle.quality_rating,
                                                     lower_limit = True)

            if checks:
                check = checks[0]
                _report_change_in_quality_rating(vehicle, check)
                vehicle.quality_rating = check.new_quality_rating
        elif margin > 0:
            checks = MaintenanceCheck.objects.filter(quality_rating = vehicle.quality_rating,
                                                     upper_limit = True)

            if checks:
                check = checks[0]
                _report_change_in_quality_rating(vehicle, check)
                vehicle.quality_rating = check.new_quality_rating

def _report_change_in_quality_rating(vehicle, check):
    if vehicle.quality_rating != check.new_quality_rating:
        log('quality of vehicle {0} has changed from {1} to {2}'.format(vehicle,
                                                                        vehicle.quality_rating,
                                                                        check.new_quality_rating),
            vehicle.owner)

