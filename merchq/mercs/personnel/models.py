from django.db import models

class Position(models.Model):
    position_name = models.CharField(max_length = 100)
    base_salary = models.IntegerField(default = 0)

class SkillLevel(models.Model):
    level_name = models.CharField(max_length = 25)
    salary_multiplier = models.FloatField(default = 1.0)

class Rank(models.Model):
    rank_name = models.CharField(max_length = 25)
    salary_multiplier = models.FloatField(default = 1.0)

class Person(models.Model):
    person_name = models.CharField(max_length = 100)
    position = models.ForeignKey(Position)
    skill_level = models.ForeignKey(SkillLevel)
    rank = models.ForeignKey(Rank)
