from django.db import models

class Parameter(models.Model):
    parameter_name = models.CharField(max_length = 50,
                                      primary_key = True)
    date_value = models.DateField(null = True,
                                  blank = True)

    def __unicode__(self):
        return '{0}:{1}'.format(self.parameter_name,
                                self.date_value)
