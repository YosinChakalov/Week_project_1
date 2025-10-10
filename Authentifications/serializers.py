from rest_framework.serializers import ModelSerializer
from .models import *
from Bookings.serializers import BookingSerializer,Booking
from Trips.serializers import TripsSerializer,Trip
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = True  
        user.save()

        
        token = RefreshToken.for_user(user).access_token

        
        verify_url = f"http://127.0.0.1:8000/api/verify/?token={token}"

        
        send_mail(
            subject="Подтверждение email",
            message=f"Нажмите на ссылку, чтобы подтвердить аккаунт: {verify_url}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return user
    
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'bio', 'user_id', 'status']
        read_only_fields = ['user_id','status']

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        bookings = Booking.objects.filter(user_id=instance.user)
        trips = Trip.objects.filter(driver_id=instance.user)
        represent['Bookings'] = BookingSerializer(bookings, many=True).data
        represent['Trips'] = TripsSerializer(trips, many=True).data
        return represent