from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('vestidos/', views.VestidoListView.as_view(), name='vestidos'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('proveedores/', views.ProveedorListView.as_view(), name='proveedores'),
    
    path('vestidos/<pk>', views.VestidoDetailView.as_view(), name='detalle-vestido'),
    path('clientes/<pk>', views.ClienteDetailView.as_view(), name='detalle-cliente'),
    path('proveedores/<pk>', views.ProveedorDetailView.as_view(), name='detalle-proveedor'),

    path('arrendados/', views.ArrendadoListView.as_view(), name='arrendados'),
    path('disponibles/', views.DisponibleListView.as_view(), name='disponibles'),
    path('mantencion/', views.MantencionListView.as_view(), name='mantencion'),
    
    path('reservas/', views.ReservaListView.as_view(), name='reservas'),
    path('devueltos/', views.DevueltoListView.as_view(), name='devueltos'),
    path('reservas/<pk>', views.ReservaDetailView.as_view(), name='detalle-reservas'),
   
    #path('reservas/<pk>/renew/', views.ingreso_reserva, name='ingreso_reserva'),
]
   
urlpatterns += [
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
]
    

    