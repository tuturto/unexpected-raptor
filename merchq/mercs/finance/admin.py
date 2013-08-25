from django.contrib import admin

from mercs.finance.models import Invoice, InvoiceRow, Product, Transaction

admin.site.register(Transaction)
admin.site.register(Invoice)
admin.site.register(InvoiceRow)
admin.site.register(Product)

