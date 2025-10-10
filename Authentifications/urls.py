from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),         
    path('login/', TokenObtainPairView.as_view()),  
    path('token/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),   
    path('profile/', ProfileView.as_view()),
    path('verify/', VerifyEmail.as_view()),
    path('profile/edit/<int:pk>', ProfileEditView.as_view()),
]