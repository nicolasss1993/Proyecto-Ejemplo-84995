from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from medicos.models import Medico


class MedicoListView(ListView):
    model = Medico
    template_name = "medicos/medico_list.html"
    context_object_name = "medicos"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset
        

class MedicoDetailView(DetailView):
    model = Medico
    template_name = "medicos/medico_detail.html"
    context_object_name = "medico"
    slug_field = "code"
    slug_url_kwarg = "code"


class MedicoCreateView(CreateView):
    model = Medico
    fields = ["nombre", "apellido", "especialidad"]
    # form_class = MedicoForm
    template_name = "medicos/medico_form.html"
    
    def get_success_url(self):
        return reverse_lazy(
            "medico_detail",
            kwargs={"code": self.object.code}
        )


class MedicoUpdateView(UpdateView):
    model = Medico
    fields = ["nombre", "apellido"]
    slug_field = "code"
    slug_url_kwarg = "code"

    def get_success_url(self):
        return reverse_lazy(
            "medico_detail",
            kwargs={"code": self.object.code}
        )


class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = "medicos/medico_confirm_delete.html"
    success_url = reverse_lazy("medico_list")
