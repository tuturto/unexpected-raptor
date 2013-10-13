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

import mercs.integration.views 

urlpatterns = patterns('',
    url(r'^current_date/$',
        mercs.integration.views.CurrentDateView.as_view()),
    url(r'^forces/$',
        mercs.integration.views.ForceList.as_view(),
        name = 'forces-list'),
    url(r'^forces/(?P<id>\d+)/$',
        mercs.integration.views.ForceDetails.as_view(),
        name = 'force-details'),
    url(r'^logs/$',
        mercs.integration.views.GMLogEntryList.as_view(),
        name = 'log-list'),
    url(r'^logs/(?P<id>\d+)/$',
        mercs.integration.views.GMLogEntryDetails.as_view(),
        name = 'log-details'),
    url(r'^cycle/$',
        mercs.integration.views.cycle,
        name = 'cycle'),
)

