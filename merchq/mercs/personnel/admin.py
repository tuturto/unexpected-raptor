from django.contrib import admin
from mercs.personnel.models import Person, Rank, Position, SkillLevel
from mercs.personnel.models import SkillDefinition, Skill

admin.site.register(Person)
admin.site.register(Rank)
admin.site.register(Position)
admin.site.register(SkillLevel)
admin.site.register(SkillDefinition)
admin.site.register(Skill)
