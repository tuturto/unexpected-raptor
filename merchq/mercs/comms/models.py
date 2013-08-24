from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.tag_name

class NewsEntry(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField(max_length = 5000)
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return '{0} - {1}'.format(self.pub_date,
                                  self.title)
