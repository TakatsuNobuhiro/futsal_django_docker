from django.contrib import admin

# Register your models here.
from .models import Player,Club


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass
