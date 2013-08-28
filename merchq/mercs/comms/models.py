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
