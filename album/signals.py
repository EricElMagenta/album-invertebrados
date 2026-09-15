from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Album

@receiver(post_save, sender=User)
def create_album(sender, instance, created, **kwargs):
    if created:
        Album.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_album(sender, instance, **kwargs):
    instance.album.save()