from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reviews',ReviewViewset,basename='reviews')

urlpatterns = [
    path('',include(router.urls))
]