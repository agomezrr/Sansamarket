
# Register your models here.
from django.contrib import admin
from .models import Resena

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calificador', 'calificacion', 'fecha')
    search_fields = ('usuario__username', 'calificador__username', 'calificacion')
    list_filter = ('calificacion', 'fecha')
    date_hierarchy = 'fecha'