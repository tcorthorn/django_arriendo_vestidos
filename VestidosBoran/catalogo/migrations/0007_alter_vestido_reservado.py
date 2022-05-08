# Generated by Django 4.0.2 on 2022-05-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_alter_reserva_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vestido',
            name='reservado',
            field=models.CharField(blank=True, choices=[('Reservado', 'Reservado'), ('Sin reserva', 'No reservado')], default='Sin reserva', help_text='Disponibilidad del vestido', max_length=15),
        ),
    ]
