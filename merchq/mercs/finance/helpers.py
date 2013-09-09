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

from __future__ import division
from mercs.finance.models import Transaction
from mercs.forces.models import Force
from mercs.common.models import Parameter
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from PIL import Image, ImageDraw

def balance(force, balance_date):
    transactions = Transaction.objects.filter(force = force,
                                              date__lte = balance_date)
    balance = sum([transaction.value for transaction
                   in transactions])

    return balance

def balance_report(force, year, month = None):

    params = Parameter.objects.filter(parameter_name = 'current date')
    current_date = params[0].date_value

    year = int(year)
    if month:
        month = int(month)

    if month:
        running_date = datetime.date(year, month, 1)
    else:
        running_date = datetime.date(year, 1, 1)

    if month:
        if month < 12:
            end_date = datetime.date(year, month + 1, 1)
        else:
            end_date = datetime.date(year + 1, 1, 1)
    else:
        if current_date.year == year:
            end_date = current_date + datetime.timedelta(1)
        else:
            end_date = datetime.date(year + 1, 1, 1)

    balances = []

    while running_date < end_date:
        balances.append([running_date.isoformat(), balance(force, running_date)])
        running_date = running_date + datetime.timedelta(1)

    return balances

