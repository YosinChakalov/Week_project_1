from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from Bookings.models import Booking
from Bookings.serializers import BookingSerializer
from .pagination import TripPagination
from .permissions import TripPermission

class TripsAPIView(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripsSerializer
    permission_classes = [IsAuthenticated,TripPermission]
    pagination_class = TripPagination

    filter_backends = [DjangoFilterBackend,SearchFilter]
    
    filterset_fields = [ 'price','date' ]

    search_fields = ['title', 'from_where', 'to_where', ]

    def perform_create(self, serializer):
        serializer.save(driver_id=self.request.user)

class DriverTripBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role != 'taxi':
            raise PermissionDenied("Only taxi drivers can view this.")

        return Booking.objects.filter(trip__driver_id=user)