from django.contrib import admin
from mercs.personnel.models import Person, Rank, Position, SkillLevel

admin.site.register(Person)
admin.site.register(Rank)
admin.site.register(Position)
admin.site.register(SkillLevel)
