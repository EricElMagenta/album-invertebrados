from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Album(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Album'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Invertebrate(models.Model):


    def __str__(self):
        return f'{self.name}.'

    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)
    taxon_class = models.CharField(max_length=50)
    taxon_order = models.CharField(max_length=50)
    facts = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='invertebrate_pics')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)