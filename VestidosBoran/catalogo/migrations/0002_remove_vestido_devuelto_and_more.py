# Generated by Django 4.0.2 on 2022-04-24 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vestido',
            name='devuelto',
        ),
        migrations.RemoveField(
            model_name='vestido',
            name='fecha_a_devolver',
        ),
    ]
