from django.contrib import admin

from models import Sport, Team, Player

class SportAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('first', 'last')
    
admin.site.register(Sport, SportAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, TeamAdmin)