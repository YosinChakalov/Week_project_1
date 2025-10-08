from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'trip_id', 'book_seats', 'is_active']
        read_only_fields = ['is_active', 'user_id']