from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class ShippingDetails(models.Model):
    """Shipping details of the user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShippingDetails.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.shippingdetails.save()
