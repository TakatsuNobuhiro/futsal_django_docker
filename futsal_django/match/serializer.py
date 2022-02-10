# coding: utf-8

from rest_framework import serializers

from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'club_id', 'first_name', 'last_name', 'uniform_number',
                  'position', 'birth_day']
