from django.contrib import admin

from mercs.armoury.models import VehicleType, WeightClass, SupportType
from mercs.armoury.models import Vehicle

admin.site.register(VehicleType)
admin.site.register(WeightClass)
admin.site.register(SupportType)
admin.site.register(Vehicle)
