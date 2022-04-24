from django.contrib import admin
from .models import Proveedor, Categoria, Vestido, Cliente,Talla

# Define the admin class
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
   
# Register the admin class with the associated model
admin.site.register(Proveedor, ProveedorAdmin)

# Register the Admin classes for Vestidos_para arriendo using the decorator

"""
class Arriendo_y_Devolucioninline(admin.TabularInline):
    model = Arriendo_y_Devolucion

@admin.register(Vestido)
class VestidoAdmin(admin.ModelAdmin):
    list_display = ('nombre','display_categoria', 'proveedor')
    inlines = [Arriendo_y_Devolucioninline]
"""

# Register the Admin classes for Arriendo_Devolucion using the decorator
"""
@admin.register(Arriendo_y_Devolucion)
class Arriendo_y_DevolucionAdmin(admin.ModelAdmin):
    list_display = ('vestido','cliente','fecha_a_devolver', 'devuelto')
    
    fieldsets = (
        (None, {'fields': ('vestido', 'cliente')}),
        
        ('Arriendo', {'fields': ('fecha_a_devolver',)}),   

        ('Devolucion', {'fields': ('devuelto',)}),
      
        #('Disponibilidad Actualizada', {'fields': ('cliente', )}),
    )

"""
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos', 'email', 'telefono')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Talla)
class TallaAdmin(admin.ModelAdmin):
    list_display = ('talla',)

@admin.register(Vestido)
class VestidoAdmin(admin.ModelAdmin):
    list_display = ('nombre','status')

