from rest_framework import serializers
from .models import *

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id','title','desc','from_where','to_where','price','seats','date','available','driver_id']
        read_only_fields = ['driver_id']