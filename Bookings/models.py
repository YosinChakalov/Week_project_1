from django.db import models

class Booking(models.Model):
    status_choices = [
        ("active","ACTIVE"),
        ("unactive","UNACTIVE")
    ]
    user_id = models.ForeignKey("Authentifications.User", on_delete=models.CASCADE)
    trip_id = models.ForeignKey("Trips.Trip", on_delete=models.CASCADE)
    book_seats = models.IntegerField()
    is_active = models.CharField(max_length=100, choices=status_choices, default='active')
