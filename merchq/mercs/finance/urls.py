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

from mercs.finance import views, helpers

urlpatterns = patterns('',
    url(r'^$',
        views.index,
        name='mercs.finance.index'),
    url(r'^(?P<force_id>\d+)/$',
        views.force_finances,
        name='mercs.finance.force'),
    url(r'^invoice/(?P<invoice_id>\d+)/$',
        views.invoice,
        name='mercs.finance.invoice'),
    url(r'^reports/(?P<force_id>\d+)/$',
        views.reports,
        name='mercs.finance.reports'),
    url(r'^reports/(?P<force_id>\d+)/(?P<year>\d{4})/$',
        views.reports,
        name='mercs.finance.reports_year'),
    url(r'^reports/(?P<force_id>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.reports,
        name='mercs.finance.reports_month'),
    url(r'^balance_chart/(?P<force_id>\d+)/(?P<year>\d{4})/$',
        helpers.balance_report,
        name='mercs.finance.balance_report_year'),
    url(r'^balance_chart/(?P<force_id>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/$',
        helpers.balance_report,
        name='mercs.finance.balance_report_month'),
)

