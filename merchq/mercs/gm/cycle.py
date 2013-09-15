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

from mercs.armoury.maintenance import run_maintenance
from mercs.personnel.models import Team
from mercs.gm.helpers import log

def run_cycle(force):
    """
    Run full cycle for a force
    """
    log('Running a cycle for force {0}'.format(force.force_name), force)

    run_maintenance(force, Team, log)

    log('Cycle finished for force {0}'.format(force.force_name), force)

