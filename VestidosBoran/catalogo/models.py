from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Categoria(models.Model):
    """
    Modelo que representa un Categoría (p. ej. Noche, Largo, Corto, Fiesta etc.)
    """
    nombre = models.CharField(max_length=200, help_text="Ingrese el nombre de la Categoría (p. ej. Noche, Largo, Corto, Fiesta etc.)")

    def __str__(self):
        return self.nombre


class Catalogo_Vestido(models.Model):
    nombre = models.CharField(max_length=200)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    # ForeignKey, ya que un vestido tiene un solo proveedor, pero el mismo proveedor puede haber confeccionado muchos tipos de vestidos.
    # 'Proveedor' es un string, en vez de un objeto, porque la clase Proveedor aún no ha sido declarada.

    detalle = models.TextField(max_length=1000, help_text="Ingrese una descripción del vestido")
    categoria = models.ManyToManyField(Categoria, help_text="Seleccione una categoría para este vestido")

    # ManyToManyField, porque una categoria puede contener muchos vestidos y un vestido puede cubrir varias categorías.
    # La clase Categoria ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        return self.nombre


    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Vestido
        """
        return reverse('detalle-vestido', args=[str(self.id)])

    def display_categoria(self):
        """
        Creates a string for the Categoría. This is required to display categoria in Admin.
        """
        return ', '.join([ categoria.nombre for categoria in self.categoria.all()[:3] ])
    display_categoria.short_description = 'Categoria'




import uuid # Requerida para las instancias de libros únicos

class Vestidos_para_arriendo(models.Model):
    """
    Modelo que representa un vestido único ingresado a tienda para ser arrendado
    """
    id = models.CharField(primary_key=True, max_length=7, default='V000000', help_text="ID único para este vestido particular en toda la tienda")
    vestido = models.ForeignKey(Catalogo_Vestido, on_delete=models.SET_NULL, null=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'En mantención'),
        ('o', 'Arrendado'),
        ('a', 'Disponible'),
        ('r', 'Reservado'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del vestido')

    class Meta:
        ordering = ["fecha_devolucion"]

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.vestido.nombre)


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle_proveedor', args=[str(self.id)])


class Cliente(models.Model):
    """
    Modelo que representa un cliente
    """
    nombre = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un cliente.
        """
        return reverse('detalle_cliente', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.apellidos, self.nombre)


