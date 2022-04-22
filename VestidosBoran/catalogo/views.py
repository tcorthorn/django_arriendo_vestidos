from django.shortcuts import render

# Create your views here.

from .models import Proveedor, Categoria, Catalogo_Vestido, Vestidos_para_arriendo, Cliente

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_vestidos=Catalogo_Vestido.objects.all().count()
    num_solicitudes=Vestidos_para_arriendo.objects.all().count()
    # Libros disponibles (status = 'a')
    num_solicitudes_disponibles=Vestidos_para_arriendo.objects.filter(status__exact='a').count()
    num_proveedores=Proveedor.objects.count()  # El 'all()' esta implícito por defecto.

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_vestidos':num_vestidos,'num_solicitudes':num_solicitudes,'num_solicitudes_disponibles':num_solicitudes_disponibles,'num_proveedores':num_proveedores},
    )
