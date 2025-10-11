from rest_framework import serializers
from .models import *
from Bookings.serializers import BookingSerializer,Booking
from Reviews.serializers import ReviewSerializer,Review

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id','title','desc','from_where','to_where','price','seats','date','available','driver_id']
        read_only_fields = ['driver_id']
    
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        bookings = Booking.objects.filter(trip_id=instance.id)
        review = Review.objects.filter(trip_id=instance.id)
        represent['Bookings'] = BookingSerializer(bookings, many=True).data
        represent['Review'] = ReviewSerializer(review, many=True).data
        return represent