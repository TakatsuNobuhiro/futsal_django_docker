# import django_filters

from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Player
from .serializer import PlayerSerializer

from rest_framework import mixins
from rest_framework import generics


class PlayerList(APIView):
    def get(self, request, foramt=None):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request, foramt=None):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PlayerList(generics.ListCreateAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer


class PlayerDetail(APIView):
    def get_object(self, id):
        try:
            return Player.objects.get(id=id)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        player = self.get_object(id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
