from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView,DetailView
from django.forms import ModelForm
from django.urls import reverse_lazy
from . models import Village
from village.form import VillageForm,SearchForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        villages = Village.objects.all()
        context['locations'] = villages
        return context


class VillageCreateView(CreateView):
    model = Village
    form_class = VillageForm
    template_name = "village_form.html"
    # fields = ['name', 'latitude', 'longitude']
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map'] = {
            'center': {'lat': 0, 'lng': 0},
            'zoom': 10
        }
        return context

class VillageDeleteView(DeleteView):
    model = Village
    template_name = "village_delete.html"
    success_url = reverse_lazy("village_list_view")


class VillageUpdateView(UpdateView):
    model = Village
    form_class = VillageForm
    template_name = "village_update.html"
    success_url = reverse_lazy("village_list_view")

class VillageListView(ListView):
    model = Village
    template_name = "village_list.html"
    delete_view = VillageDeleteView
    update_view = VillageUpdateView
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search']
            queryset = queryset.filter(name__icontains=search_query)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
    

class VillageDetailView(DetailView):
    model = Village
    template_name = 'village_detail.html'
    
