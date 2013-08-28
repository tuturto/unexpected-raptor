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

from django.db import models

from mercs.forces.models import Force

class Invoice(models.Model):
    force = models.ForeignKey(Force)
    date = models.DateField()

    def value(self):
        invoices = self.invoicerow_set.all()
        total = sum([inv.value() for inv in invoices])
        return total

    def __unicode__(self):
        return '{0}: {1}'.format(self.force,
                                 self.value())

class Product(models.Model):
    product_name = models.CharField(max_length = 50)    

    def __unicode__(self):
        return self.product_name

class InvoiceRow(models.Model):
    amount = models.IntegerField(default = 0)
    product = models.ForeignKey(Product)
    price = models.IntegerField(default = 0)
    note = models.CharField(max_length = 50,
                            null = True,
                            blank = True)
    invoice = models.ForeignKey(Invoice)

    def value(self):
        return self.price * self.amount

    def __unicode__(self):
        return '{0} {1}, {2} price per piece, total: {3} ({4})'.format(self.amount,
                                                                       self.product,
                                                                       self.price,
                                                                       self.value(),
                                                                       self.note)

class Transaction(models.Model):
    force = models.ForeignKey(Force)
    value = models.IntegerField(default = 0)
    date = models.DateField()
    note = models.TextField(max_length = 250)
    invoice = models.ForeignKey(Invoice,
                                null = True,
                                blank = True)

    def __unicode__(self):
        return '{0} {1} : {2}'.format(self.force.force_name,
                                      self.date,
                                      self.value)

