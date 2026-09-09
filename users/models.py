from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # Recibe la url de una imagen y se guarda en el directorio "profile_pics"

    def __str__(self):
        return f'{self.user.username} Profile'

# Profile hereda de models.Model y usando "super" podemos usar métodos
# de la clase padre
    def save(self):
        super().save()

# Cambiando el tamaño de la imagen de perfil
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)