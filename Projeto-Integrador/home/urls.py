from django.urls import path
from . import views

urlpatterns = [
    path('ca/', views.ca_add, name="ca_add"),
    path('ca_update/<int:id>', views.ca_update, name="ca_update"),
    path('ca_delete/<int:id>', views.ca_delete, name="ca_delete"),

    path('epi/', views.epi_add, name="epi_add"),
    path('epi_update/<int:id>', views.epi_update, name="epi_update"),
    path('epi_delete/<int:id>', views.epi_delete, name="epi_delete"),
    
    path('colaborador/', views.colaborador_add, name="colaborador_add"),
    path('colaborador_update/<int:id>', views.colaborador_update, name="colaborador"),
    path('colaborador_delete/<int:id>', views.colaborador_delete, name="colaborador_delete"),
    
    path('estoque/', views.estoque_add, name="estoque_add"),
    path('estoque_update/<int:id>', views.estoque_update, name="estoque_update"),
    path('estoque_delete/<int:id>', views.estoque_delete, name="estoque_delete"),

    path('entrega/', views.entrega_add, name="entrega_add"),
    path('entrega_update/<int:id>', views.entrega_update, name="entrega_update"),
    path('entrega_delete/<int:id>', views.entrega_delete, name="entrega_delete"),




]