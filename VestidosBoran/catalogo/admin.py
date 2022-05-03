from django.contrib import admin
from .models import Arriendo, Proveedor, Categoria, Vestido, Cliente,Talla
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from datetime import date

class GastosResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        model = Cliente
        model = Categoria
        model = Talla
        model = Vestido
        model = Arriendo

# Define the admin class
class ProveedorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    resources_class=Proveedor
    search_fields=("nombre", )
    
# Register the admin class with the associated model
admin.site.register(Proveedor, ProveedorAdmin)

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','apellidos','rut', 'email', 'telefono')
    list_filter = ('apellidos', 'nombre')
    resources_class=Cliente
    search_fields=("nombre", )

@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre',)
    resources_class=Categoria
    search_fields=("nombre", )

@admin.register(Talla)
class TallaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('talla',)
    resources_class=Talla
    search_fields=("nombre", )

#class ArriendoInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    #model = Arriendo

@admin.register(Vestido)
class VestidoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sku','nombre',  'status', 'display_talla', 'display_categoria','proveedor' )
    list_filter = ('status','talla','categoria')
    resources_class=Vestido
    search_fields=('fecha_a_devolver', )
    #inlines = [ArriendoInline]



@admin.register(Arriendo)
class ArriendoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sku','status','display_cliente','display_cliente2','fecha_inicio_arriendo','fecha_a_devolver','fecha_que_devolvio','valor_pagado','fecha_de_pago','creado', 'modificado','comentario')
    list_filter = ('status','sku',)
    resources_class=Arriendo
    search_fields=("cliente", )

    


