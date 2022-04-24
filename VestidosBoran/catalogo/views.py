from django.shortcuts import render

# Create your views here.

from .models import Proveedor, Categoria, Vestido,  Cliente

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    vestidos=Vestido.objects.all().count()
    clientes=Cliente.objects.all().count()
    vestidos_disponibles=Vestido.objects.filter(status='d').count()
    vestidos_arrendados=Vestido.objects.filter(status='a').count()
    vestidos_mantencion=Vestido.objects.filter(status='m').count()
    vestidos_reservados=Vestido.objects.filter(status='r').count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
        'vestidos':vestidos,
        'clientes':clientes,
        'vestidos_disponibles':vestidos_disponibles, 
        'vestidos_arrendados':vestidos_arrendados,
        'vestidos_mantencion':vestidos_mantencion,
        'vestidos_reservados':vestidos_reservados,
        }
    )

from django.views import generic

class VestidoListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    

class VestidoDetailView(generic.DetailView):
    model = Vestido
    paginate_by = 10

class ArrendadoListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='a') #vestidos arrendados
    template_name = 'Vestido/arriendo_list.html'  # Specify your own template name/location

class DisponibleListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='d') #vestidos disponibles
    template_name = 'Vestido/disponible_list.html'  # Specify your own template name/location

class ReservadoListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='r') #vestidos reservados
    template_name = 'Vestido/reservado_list.html'  # Specify your own template name/location

class MantencionListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='m') #vestidos mantencion
    template_name = 'Vestido/mantencion_list.html'  # Specify your own template name/location