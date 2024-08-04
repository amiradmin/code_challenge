# users/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Represents a profile associated with a user.

    Attributes:
    -----------
    user : User
        The user to whom this profile belongs. This is a one-to-one relationship.
    bio : str
        A short biography of the user.
    location : str
        The location of the user.
    birth_date : date
        The birth date of the user.
    mobile : str
        The mobile phone number of the user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()