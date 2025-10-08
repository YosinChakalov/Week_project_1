from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):
    Choises = (
        ('admin', 'Admin'),
        ('taxi', 'TAXI'),
        ('user', 'USER'),
    )
    role = models.CharField(max_length=20, choices=Choises, default='user')
    email = models.CharField(unique=True)
    username = models.CharField(null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=50,default='user')

    def __str__(self):
        return f"{self.name}'s profile"