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

from mercs.gm.models import GMLogEntry
from mercs.common.models import Parameter

def log(text, force):
    param = Parameter.objects.filter(parameter_name = 'current date')[0]   

    log_entry = GMLogEntry()
    log_entry.entry_date = param.date_value
    log_entry.text = text
    log_entry.force = force

    log_entry.save()

