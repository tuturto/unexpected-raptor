from django.db import models

class Time(models.Model):
    current_time = models.DateField()

    def __unicode__(self):
        return str(self.current_time)
