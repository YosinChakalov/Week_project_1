from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Bookings

@receiver(pre_save, sender=Bookings)
def store_old_status(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Bookings.objects.get(pk=instance.pk)
        instance._old_status = old_instance.status
    else:
        instance._old_status = None

@receiver(post_save, sender=Bookings)
def tripBooking(sender, instance, created, **kwargs):
    trip = instance.trip

    if created and instance.status == 'active':
        trip.seats -= instance.seats_quantity
        trip.save()

    elif not created and instance.status == 'cancelled' and instance._old_status == 'active':
        trip.seats += instance.seats_quantity
        trip.save()

@receiver(post_delete, sender=Bookings)
def tripBookingDelete(sender, instance, **kwargs):
    trip = instance.trip
    if instance.status == 'active':
        trip.seats += instance.seats_quantity
        trip.save()