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

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from mercs.forces.models import Force
from mercs.finance.models import Transaction, Invoice
from mercs.common.models import Parameter
from mercs.finance.helpers import balance

def index(request):
    forces = Force.objects.all()

    balance_date = Parameter.objects.filter(parameter_name = 'current date')[0].date_value

    force_data = []

    for force in forces:        
        force_data.append([force, balance(force, balance_date)])

    context = {'forces': force_data}

    return render(request, 'finances/index.html', context)

def force_finances(request, force_id):
    force = get_object_or_404(Force, id = force_id)

    transactions = Transaction.objects.filter(force = force)

    balance_date = Parameter.objects.filter(parameter_name = 'current date')[0].date_value

    context = {'force': force,
               'transactions': transactions,
               'balance': balance(force, balance_date)}

    return render(request, 'finances/force_finances.html', context)

def invoice(request, invoice_id):
    
    invoice = get_object_or_404(Invoice, id = invoice_id)

    context = {'invoice': invoice}

    return render(request, 'finances/invoice.html', context)

def reports(request, force_id):
    force = get_object_or_404(Force, id = force_id)

    context = {'force': force,
               'year': 3068}

    return render(request, 'finances/balance_report.html', context)

