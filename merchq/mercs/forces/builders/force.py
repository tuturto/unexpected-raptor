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

from mercs.forces.models import Force

class ForceBuilder(object):

    def __init__(self):
        super(ForceBuilder, self).__init__()

        self.force_name = 'generic force'

    def with_name(self, force_name):
        self.force_name = force_name
        return self

    def build(self):
        new_force = Force()
        new_force.force_name = self.force_name

        return new_force

    def build_and_save(self):
        new_force = self.build()

        new_force.save()

        return new_force

