from django.db import models

class Position(models.Model):
    position_name = models.CharField(max_length = 100)
    base_salary = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.position_name

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

    def __unicode__(self):
        return '{0} {1} {2} {3}'.format(self.skill_level,
                                        self.position,
                                        self.rank,
                                        self.person_name)
