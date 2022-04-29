# Generated by Django 4.0.2 on 2022-04-25 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre de la Categoría (p. ej. Noche, Largo, Corto, Fiesta etc.)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Otro', help_text='Ingrese quien confeccionó el vestido', max_length=100)),
                ('email', models.EmailField(blank=True, help_text='Opcional', max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, help_text='Opcional', max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(help_text='Ingrese la talla', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vestido',
            fields=[
                ('nombre', models.CharField(max_length=200)),
                ('id', models.CharField(default='V000000', help_text='ID único para este vestido particular en toda la tienda', max_length=7, primary_key=True, serialize=False)),
                ('detalle', models.TextField(help_text='Ingrese una descripción del vestido', max_length=1000)),
                ('fecha_a_devolver', models.DateField(blank=True, help_text='Fecha que debe devolver el vestido', null=True)),
                ('devuelto', models.DateField(blank=True, help_text='Fecha cuando devolvió el vestido', null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'En mantención'), ('a', 'Arrendado'), ('d', 'Disponible'), ('r', 'Reservado')], default='m', help_text='Disponibilidad del vestido', max_length=1)),
                ('categoria', models.ManyToManyField(help_text='Seleccione una categoría para este vestido', to='catalogo.Categoria')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.cliente')),
                ('proveedor', models.ForeignKey(default='Otro', help_text='Opcional', on_delete=django.db.models.deletion.CASCADE, to='catalogo.proveedor')),
                ('talla', models.ManyToManyField(help_text='Seleccione una talla para este vestido', to='catalogo.Talla')),
            ],
        ),
    ]
