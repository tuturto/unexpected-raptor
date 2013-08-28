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

from mercs.finance.models import Invoice, InvoiceRow, Transaction
from mercs.common.models import Parameter

def sell_vehicle(vehicle, price):
  
    trans_date = Parameter.objects.filter(parameter_name = 'current date')[0].date_value

    trans = Transaction()
    trans.force = vehicle.owner
    trans.value = price
    trans.date = trans_date
    trans.note = 'sale {0}'.format(vehicle.vehicle_name)

    vehicle.active = False
    vehicle.owner = None

    vehicle.save()
    trans.save()

