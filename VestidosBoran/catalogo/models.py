from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Categoria(models.Model):
    """     Modelo que representa un Categoría (p. ej. Noche, Largo, Corto, Fiesta etc.)     """

    nombre = models.CharField(max_length=100, help_text="Ingrese el nombre de la Categoría (p. ej. Noche, Largo, Corto, Fiesta etc.)")

    def __str__(self):
        return self.nombre

class Talla(models.Model):
    """     Modelo que representa un Talla     """

    talla = models.CharField(max_length=100, help_text="Ingrese la talla")

    def __str__(self):
        return self.talla

class Catalogo(models.Model):
    nombre = models.CharField(max_length=200)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True,default='Otro' , help_text="Opcional")

    # ForeignKey, ya que un vestido tiene un solo proveedor, pero el mismo proveedor puede haber confeccionado muchos tipos de vestidos.
    # 'Proveedor' es un string, en vez de un objeto, porque la clase Proveedor aún no ha sido declarada.

    id = models.CharField(primary_key=True, max_length=7, default='V000000', help_text="ID único para este vestido particular en toda la tienda")

    detalle = models.TextField(max_length=1000, help_text="Ingrese una descripción del vestido")
    categoria = models.ManyToManyField(Categoria, help_text="Seleccione una categoría para este vestido")
    talla = models.ManyToManyField(Talla, help_text="Seleccione una talla para este vestido")

    LOAN_STATUS = (
        ('m', 'En mantención'),
        ('a', 'Arrendado'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Disponibilidad del vestido')

    # ManyToManyField, porque una categoria puede contener muchos vestidos y un vestido puede cubrir varias categorías.
    # La clase Categoria ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        return self.nombre

    class Meta():
        verbose_name='catalogo'
        verbose_name_plural ='catalogo'


    def get_absolute_url(self):
        """         Devuelve el URL a una instancia particular de Vestido         """

        return reverse('detalle-vestido', args=[str(self.id)])

    def display_categoria(self):
        """"         Creates a string for the Categoría. This is required to display categoria in Admin.        """

        return ', '.join([ categoria.nombre for categoria in self.categoria.all()[:3] ])
    display_categoria.short_description = 'Categoria'


class Arriendo_y_Devolucion(models.Model):
    """     Modelo que representa un vestido único ingresado a tienda para ser arrendado     """

    id = models.CharField(primary_key=True, max_length=7, default='V000000', help_text="ID único para este vestido particular en toda la tienda")
    vestido = models.ForeignKey(Catalogo, on_delete=models.SET_NULL, null=True)
    fecha_a_devolver = models.DateField(null=True, blank=True , help_text="Fecha que debe devolver el vestido")
    devuelto = models.DateField(null=True, blank=True , help_text="Fecha cuando devolvió el vestido")
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True,)

    LOAN_STATUS = (
        ('m', 'En mantención'),
        ('a', 'Arrendado'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Disponibilidad actualizada del vestido')

    class Meta:
        ordering = ["fecha_a_devolver"]

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.vestido)

    class Meta():
        verbose_name='Arriendo_y_devolucion'
        verbose_name_plural ='Arriendo_y_devoluciones'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, default='Otro', help_text='Ingrese quien confeccionó el vestido')
    email = models.EmailField(null=True,blank=True, help_text='Opcional')
    telefono = models.CharField(max_length=10,null=True,blank=True , help_text='Opcional')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle_proveedor', args=[str(self.id)])

    class Meta():
        verbose_name='proveedor'
        verbose_name_plural ='Proveedores'

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


