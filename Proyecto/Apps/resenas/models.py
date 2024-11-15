from django.db import models
from django.contrib.auth.models import User

class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resenas_recibidas')
    calificador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resenas_realizadas')
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.calificador.username} -> {self.usuario.username}: {self.calificacion}'
# Create your models here.
