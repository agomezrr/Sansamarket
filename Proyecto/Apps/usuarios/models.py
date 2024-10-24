from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)  # Nuevo campo de biografía

    def __str__(self):
        return self.user.username