from django.contrib import admin

# Register your models here.
from .models import Player, Club, Game, Place, Goal, Node, Category, Season, \
    League, Shoot, Member, Warning, Staff


@admin.register(Player, Game, Club, Place, Goal, Node, Category, Season, League,
                Shoot, Member, Warning, Staff)
class PlayerAdmin(admin.ModelAdmin):
    pass

# @admin.register(Club)
# class ClubAdmin(admin.ModelAdmin):
#     pass
