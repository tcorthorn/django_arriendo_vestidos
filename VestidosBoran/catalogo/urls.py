from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('vestidos/', views.VestidoListView.as_view(), name='vestidos'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),

    path('vestidos/<pk>', views.VestidoDetailView.as_view(), name='detalle-vestido'),
    path('clientes/<pk>', views.ClienteDetailView.as_view(), name='detalle-cliente'),

    path('arrendados/', views.ArrendadoListView.as_view(), name='arrendados'),
    #path('arrendados/<pk>', views.ArrendadoDetailView.as_view(), name='detalle-vestido'),
    path('disponibles/', views.DisponibleListView.as_view(), name='disponibles'),
    #path('disponibles/<pk>', views.DisponibleDetailView.as_view(), name='detalle-disponible'),
    path('reservados/', views.ReservadoListView.as_view(), name='reservados'),
    #path('reservados/<pk>', views.ReservadoDetailView.as_view(), name='detalle-reservado'),
    path('mantencion/', views.MantencionListView.as_view(), name='mantencion'),
    #path('mantencion/<pk>', views.MantencionDetailView.as_view(), name='detalle-mantencion'),
]


