# -*- coding: utf-8 -*-

#   Copyright 2013 Tuukka Turto
#
#   This file is part of unexpected-raptor.
#
#   unexpected-raptor is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   unexpected-raptor is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with unexpected-raptor.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url

from mercs.gm import views

urlpatterns = patterns('',
    url(r'^$',
        views.index,
        name='mercs.gm.index'),
    url(r'^log/$',
        views.gm_log,
        name='mercs.gm.log'),
    url(r'^log/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        views.gm_log,
        name='mercs.gm.log.archive'),
    url(r'^cycle/$',
        views.gm_cycle,
        name='mercs.gm.cycle_action'),
    url(r'^log_entries/(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        views.log_entries,
        name='mercs.gm.log_entries'),
    url(r'^log_entries/$',
        views.log_entries,
        name='mercs.gm.log_entries'),
)

