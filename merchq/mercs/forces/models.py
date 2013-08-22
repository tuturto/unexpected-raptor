from django.db import models

class Force(models.Model):
    force_name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.force_name
