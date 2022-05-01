from django.shortcuts import render

# Create your views here.

from .models import Proveedor, Categoria, Vestido,  Cliente, Arriendo

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    vestidos=Vestido.objects.all().count()
    clientes=Cliente.objects.all().count()
    proveedores=Proveedor.objects.all().count()

    vestidos_disponibles=Arriendo.objects.filter(status='disponible').count()
    vestidos_arrendados=Arriendo.objects.filter(status='arrendado').count()
    vestidos_mantencion=Arriendo.objects.filter(status='mantencion').count()
    vestidos_reservados=Arriendo.objects.filter(status='reservado').count()
    vestidos_devueltos=Arriendo.objects.filter(status='devuelto').count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
        'vestidos':vestidos,
        'clientes':clientes,
        'proveedores':proveedores,
        'vestidos_disponibles':vestidos_disponibles, 
        'vestidos_arrendados':vestidos_arrendados,
        'vestidos_mantencion':vestidos_mantencion,
        'vestidos_reservados':vestidos_reservados,
        'vestidos_devueltos':vestidos_devueltos,
        }
    )

from django.views import generic

class VestidoListView(generic.ListView):
    model = Vestido
    paginate_by = 10

class ClienteListView(generic.ListView):
    model = Cliente
    paginate_by = 10 

class VestidoDetailView(generic.DetailView):
    model = Vestido
    paginate_by = 10

class ProveedorListView(generic.ListView):
    model = Proveedor
    paginate_by = 10

class ClienteDetailView(generic.DetailView):
    model = Cliente
    paginate_by = 10

class ProveedorDetailView(generic.DetailView):
    model = Proveedor
    paginate_by = 10

class ArrendadoListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='arrendado') #vestidos arrendados
    template_name = 'Vestido/arriendo_list.html'  # Specify your own template name/location

class DisponibleListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='disponible') #vestidos disponibles
    template_name = 'Vestido/disponible_list.html'  # Specify your own template name/location

class ReservadoListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='reservado') #vestidos reservados
    template_name = 'Vestido/reservado_list.html'  # Specify your own template name/location

class MantencionListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='mantencion') #vestidos mantencion
    template_name = 'Vestido/mantencion_list.html'  # Specify your own template name/location

class DevueltoListView(generic.ListView):
    model = Arriendo
    paginate_by = 10
    queryset = Arriendo.objects.filter(status__icontains='devuelto') #vestidos devueltos
    template_name = 'Arriendo/devuelto_list.html'  # Specify your own template name/location