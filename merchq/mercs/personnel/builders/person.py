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

from mercs.personnel.models import Position, Person, SkillLevel, Rank
from mercs.forces.builders import ForceBuilder
from mercs.astrography.builders import PlanetBuilder

class PersonBuilder(object):

    def __init__(self, team_builder):
        super(PersonBuilder, self).__init__()

        self.person_name = 'generic person'
        self.position = PositionBuilder().build()
        self.skill_level = SkillLevelBuilder().build()
        self.rank = RankBuilder().build()
        self.force = ForceBuilder().build()
        self.location = PlanetBuilder().build()
        self.image = 'generic image'


    def with_team(self, team):
        self.team = team
        return self

    def with_location(self, location):
        self.location = location
        return self

    def build(self):
        new_person = Person()
        new_person.person_name = self.person_name
        new_person.position = self.position
        new_person.skill_level = self.skill_level
        new_person.rank = self.rank
        new_person.force = self.force
        new_person.team = self.team
        new_person.location = self.location
        new_person.image = self.image

        return new_person

    def build_and_save(self):
        new_person = self.build()
        new_person.save()
        return new_person

class PositionBuilder(object):

    def __init__(self):
        super(PositionBuilder, self).__init__()

        self.position_name = 'generic position'
        self.base_salary = 1000

    def build(self):
        new_position = Position()
        new_position.position_name = self.position_name
        new_position.base_salary = self.base_salary

        return new_position

    def build_and_save(self):
        new_position = self.build()
        new_position.save()
        return new_position

class SkillLevelBuilder(object):

    def __init__(self):
        super(SkillLevelBuilder, self).__init__()

        self.level_name = 'generic skill level'
        self.salary_multiplier = 1

    def build(self):
        new_level = SkillLevel()
        new_level.level_name = self.level_name
        new_level.salary_multiplier = self.salary_multiplier
        return new_level

    def build_and_save(self):
        new_level = self.build()
        new_level.save()

        return new_level

class RankBuilder(object):

    def __init__(self):
        super(RankBuilder, self).__init__()

        self.rank_name = 'generic rank'
        self.salary_multiplier = 1

    def build(self):
        new_rank = Rank()
        new_rank.rank_name = self.rank_name
        new_rank.salary_multiplier = self.salary_multiplier
        return new_rank

    def build_and_save(self):
        new_rank = self.build()
        new_rank.save()

        return new_rank

