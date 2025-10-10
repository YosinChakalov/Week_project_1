from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Trips', TripsAPIView, basename='trips')

urlpatterns = [
    path('', include(router.urls)),
    path('my-trip-bookings/', DriverTripBookingsView.as_view()),
]