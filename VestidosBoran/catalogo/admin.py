from django.contrib import admin
from .models import Proveedor, Categoria, Catalogo_Vestido, Vestidos_para_arriendo, Cliente

# Define the admin class
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombre', 'email', 'telefono')
   
# Register the admin class with the associated model
admin.site.register(Proveedor, ProveedorAdmin)

# Register the Admin classes for Vestido using the decorator

class Vestidos_para_arriendoinline(admin.TabularInline):
    model = Vestidos_para_arriendo

@admin.register(Catalogo_Vestido)
class Catalogo_VestidoAdmin(admin.ModelAdmin):
    list_display = ('nombre','display_categoria', 'proveedor')
    inlines = [Vestidos_para_arriendoinline]



# Register the Admin classes for BookInstance using the decorator

@admin.register(Vestidos_para_arriendo)
class Vestidos_para_arriendoAdmin(admin.ModelAdmin):
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
