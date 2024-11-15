from django import template

register = template.Library()

@register.filter
def sum_calificaciones(queryset):
    return sum(item.calificacion for item in queryset)

@register.filter
def promedio_calificaciones(queryset):
    total = queryset.count()
    if total == 0:
        return 0
    suma = sum(item.calificacion for item in queryset)
    promedio = suma / total
    return round(promedio, 1)