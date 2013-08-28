# -*- coding: utf-8 -*-

#   Copyright 2013 Tuukka Turto
#
#   This file is part of mercs.
#
#   mercs is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   mercs is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with pyherc.  If not, see <http://www.gnu.org/licenses/>.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from mercs.forces.models import Force
from mercs.finance.models import Transaction, Invoice

def index(request):
    forces = Force.objects.all()
    transactions = Transaction.objects.all()

    force_data = []

    for force in forces:        
        balance = sum([transaction.value for transaction
                       in transactions
                       if transaction.force == force])
        force_data.append([force, balance])

    context = {'forces': force_data}

    return render(request, 'finances/index.html', context)

def force_finances(request, force_id):
    force = get_object_or_404(Force, id = force_id)
    transactions = Transaction.objects.filter(force = force_id)
    balance = sum([transaction.value for transaction
                   in transactions])

    context = {'force': force,
               'transactions': transactions,
               'balance': balance}

    return render(request, 'finances/force_finances.html', context)

def invoice(request, invoice_id):
    
    invoice = get_object_or_404(Invoice, id = invoice_id)

    context = {'invoice': invoice}

    return render(request, 'finances/invoice.html', context)

