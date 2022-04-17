from django.contrib import admin
from .models import Proveedor, Categoria, Vestido, Arriendo_vestido, Cliente

# Define the admin class
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombre', 'email', 'telefono')
   
# Register the admin class with the associated model
admin.site.register(Proveedor, ProveedorAdmin)

# Register the Admin classes for Vestido using the decorator

class Arriendo_vestidoInline(admin.TabularInline):
    model = Arriendo_vestido

@admin.register(Vestido)
class VestidoAdmin(admin.ModelAdmin):
    list_display = ('nombre','display_categoria', 'proveedor')
    inlines = [Arriendo_vestidoInline]



# Register the Admin classes for BookInstance using the decorator

@admin.register(Arriendo_vestido)
class Arriendo_vestidoAdmin(admin.ModelAdmin):
    list_display = ('vestido','fecha_devolucion')

    fieldsets = (
        (None, {
            'fields': ('vestido', 'id')
        }),
        ('Disponibilidad', {
            'fields': ('status', 'fecha_devolucion')
        }),
    )


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombre', 'email', 'telefono')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


#admin.site.register(Vestido)
#admin.site.register(Proveedor)
#admin.site.register(Categoria)
#admin.site.register(Arriendo_vestido)
#admin.site.register(Cliente)
