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

def balance_report(request, force_id, year):

    image_width = 700
    image_heigth = 400

    params = Parameter.objects.filter(parameter_name = 'current date')
    current_date = params[0].date_value

    year = int(year)
    force = get_object_or_404(Force, id = force_id)
    running_date = datetime.date(year, 1, 1)

    if current_date.year == year:
        end_date = current_date
    else:
        end_date = datetime.date(year + 1, 1, 1)

    balances = []

    while running_date < end_date:
        balances.append(balance(force, running_date))
        running_date = running_date + datetime.timedelta(1)

    pixel_per_date = image_width / 366
    max_balance = max(balances)
    if max_balance:
        pixel_per_credit = image_heigth / max_balances
    else:
        pixel_per_credit = 0

    image = Image.new("RGB", (image_width, image_heigth), 'white')

    draw = ImageDraw.Draw(image)
    draw.line([0, 0, 0, image_heigth], fill = 'blue')
    draw.line([0, image_heigth - 1, image_width, image_heigth - 1], fill = 'blue')

    day_counter = 0
    coords = []

    for bal in balances:
        day_counter = day_counter + 1
        coords.append(int(day_counter * pixel_per_date))
        coords.append(image_heigth - int(bal * pixel_per_credit))

    draw.line(coords, fill = 'red')

    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    return response

