from django.db import models
import mercs.forces.models

class Position(models.Model):
    position_name = models.CharField(max_length = 100)
    base_salary = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.position_name

class SkillDefinition(models.Model):
    skill_name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.skill_name

class SkillLevel(models.Model):
    level_name = models.CharField(max_length = 25)
    salary_multiplier = models.FloatField(default = 1.0)

    def __unicode__(self):
        return self.level_name

class Rank(models.Model):
    rank_name = models.CharField(max_length = 25)
    salary_multiplier = models.FloatField(default = 1.0)

    def __unicode__(self):
        return self.rank_name

class Person(models.Model):
    person_name = models.CharField(max_length = 100)
    position = models.ForeignKey(Position)
    skill_level = models.ForeignKey(SkillLevel)
    rank = models.ForeignKey(Rank)    
    force = models.ForeignKey(mercs.forces.models.Force,
                              null = True,
                              blank = True)

    def get_salary(self):
        return (self.position.base_salary *
                self.rank.salary_multiplier *
                self.skill_level.salary_multiplier)
    
    def __unicode__(self):
        return '{0} {1} {2} {3}'.format(self.skill_level,
                                        self.position,
                                        self.rank,
                                        self.person_name)

class Skill(models.Model):
    skill_definition = models.ForeignKey(SkillDefinition)
    person = models.ForeignKey(Person)
    skill_score = models.IntegerField(default = 0)

    def __unicode__(self):
        return '{0}-{1}: {2}'.format(self.person.person_name,
                                     self.skill_definition,
                                     self.skill_score)
