from django.urls import path
from medicos.views import *


urlpatterns = [
    path("", MedicoListView.as_view(), name="medico_list"),
    path("/crear/", MedicoCreateView.as_view(), name="medico_create"),
    path("/<slug:code>/", MedicoDetailView.as_view(), name="medico_detail"),
    path("/<slug:code>/editar/", MedicoUpdateView.as_view(), name="medico_update"),
    path("/<int:pk>/eliminar/", MedicoDeleteView.as_view(), name="medico_delete"),
]
