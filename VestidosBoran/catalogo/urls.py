from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('vestidos/', views.VestidoListView.as_view(), name='vestidos'),
    path('vestidos/<pk>', views.VestidoDetailView.as_view(), name='detalle-vestido'),
]


