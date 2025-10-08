from django.db import models

class Trip(models.Model):
    CHOICES = [
        ('available',"AVAILABLE"),
        ('unavailable',"UNAVAILABLE")
    ]
    title = models.CharField(max_length=100)
    desc = models.TextField()
    from_where = models.CharField(max_length=250)
    to_where = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    seats = models.IntegerField(default=4)
    price = models.IntegerField()
    available = models.CharField(max_length=60, choices=CHOICES, default='available')
    driver_id = models.ForeignKey("Authentifications.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title