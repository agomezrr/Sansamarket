# Generated by Django 5.1.1 on 2024-11-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_perfil_bio_remove_perfil_ubicacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='email_contacto',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
