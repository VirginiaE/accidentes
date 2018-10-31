from django.urls import path, include
from accidentes import views

urlpatterns = [
    path('', views.AccidentesListView.as_view(), name='accidentes_list'),
    path('accidente/<int:id_accidente>', views.accidente_detail, name='accidente_detail'),
    path('registrar_accidente', views.registrar_accidente, name='registrar_accidente'),
]