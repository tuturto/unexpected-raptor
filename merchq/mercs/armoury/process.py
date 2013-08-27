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

