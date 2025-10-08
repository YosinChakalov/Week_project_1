from django.db import models

class Review(models.Model):
    RATING_CHOICES = [
        ('0.5',"TERRIBLE"),
        ('1',"AWFUL"),
        ('1.5',"VERY POOR"),
        ('2',"POOR"),
        ('2.5',"BELOW AVERAGE"),
        ('3',"AVERAGE"),
        ('3.5',"DECENT"),
        ('4',"GOOD"),
        ('4.5',"VERY GOOD"),
        ('5',"EXCELENT"),
    ]
    user = models.ForeignKey('Authentifications.User', on_delete=models.CASCADE)
    trip_id = models.ForeignKey("Trips.Trip", on_delete=models.CASCADE)
    rating = models.CharField(max_length=50, choices=RATING_CHOICES, default='3')
    feed_back = models.TextField()