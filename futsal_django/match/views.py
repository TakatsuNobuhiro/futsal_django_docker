# import django_filters

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Member, Club
from .serializer import MemberSerializer, ClubSerializer


class MemberList(APIView):
    def get(self, request, foramt=None):
        players = Member.objects.all()
        serializer = MemberSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request, foramt=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClubList(APIView):
    def get(self, request, foramt=None):
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)
