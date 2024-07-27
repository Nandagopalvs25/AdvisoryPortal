from django.shortcuts import render
from website.models import CustomUser
from rest_framework import generics
from .serializers import ListUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserView(generics.ListAPIView):
    queryset= CustomUser.objects.filter(role="S")
    serializer_class= ListUserSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['batch__batch_code']
    search_fields = ['username']