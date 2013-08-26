from django.db import models
from mercs.forces.models import Force

class VehicleType(models.Model):
    type_name = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.type_name

class WeightClass(models.Model):
    weight_class = models.CharField(max_length = 50)
    vehicle_type = models.ForeignKey(VehicleType)
    lower_limit = models.IntegerField(default = 0)
    upper_limit = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return '{0} {1} ({2} - {3})'.format(self.weight_class,
                                            self.vehicle_type,
                                            self.lower_limit,
                                            self.upper_limit)

class SupportType(models.Model):
    support_name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.support_name

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length = 50)
    vehicle_type = models.ForeignKey(VehicleType)
    vehicle_weight = models.IntegerField(default = 0)

    weekly_maintenance_cost = models.IntegerField(default = 0)
    weekly_support = models.FloatField(default = 0)
    support_type = models.ForeignKey(SupportType)
    owner = models.ForeignKey(Force)
    base_price = models.IntegerField(default = 0)

    def __unicode__(self):
        return '{0} ({1})'.format(self.vehicle_name,
                                  self.id)

