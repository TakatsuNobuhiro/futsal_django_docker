# coding: utf-8

from rest_framework import serializers

from .models import Member


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'club_id', 'first_name', 'last_name', 'uniform_number',
                  'position', 'birth_day']
