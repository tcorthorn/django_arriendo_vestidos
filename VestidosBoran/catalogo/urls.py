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
]     
     #path('arriendos/<pk>', views.ArrendadoDetailView.as_view(), name='detalle-arriendo'),
    #path('arrendados/<pk>', views.ArrendadoDetailView.as_view(), name='detalle-vestido'),
    #path('disponibles/<pk>', views.DisponibleDetailView.as_view(), name='detalle-disponible'),
    
    #path('mantencion/<pk>', views.MantencionDetailView.as_view(), name='detalle-mantencion'),