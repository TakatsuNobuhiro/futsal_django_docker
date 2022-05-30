from django.contrib import admin

# Register your models here.
from .models import Member, Club, League


@admin.register(Member, Club, League, )
class PlayerAdmin(admin.ModelAdmin):
    pass

# @admin.register(Club)
# class ClubAdmin(admin.ModelAdmin):
#     pass
