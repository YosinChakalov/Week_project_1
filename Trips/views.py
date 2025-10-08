from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class TripsAPIView(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripsSerializer
    permission_classes = [IsAuthenticated]