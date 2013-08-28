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

from django.conf.urls import patterns, url

from mercs.personnel import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<force_id>\d+)/$', views.force_personnel, name='force_personnel'),
    url(r'^person/(?P<person_id>\d+)/$', views.person_details, name='person_details'),
)
