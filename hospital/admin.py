from django.contrib import admin
from hospital.models import *


#admin.site.register(DepartamentoMedico)

@admin.register(DepartamentoMedico)
class DepartamentoMedicoAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("nombre", "nro_departamento", "email_dpto", "fecha_de_creacion")
    # Columnas con enlaces clickeables para entra en el detalle
    list_display_links = ("nombre",)
    # Campos por los que se pueden buscar
    search_fields = ("nro_departamento",)
    # Filtros larelares
    list_filter = ("fecha_de_creacion",)
    # Orden por defecto
    ordering = ("nro_departamento", "nombre")
    # Campos de solo lectura
    readonly_fields = ("fecha_de_creacion",)
