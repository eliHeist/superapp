from django.contrib.auth.mixins import LoginRequiredMixin
from services.forms import ServiceModelForm
from django.shortcuts import reverse, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Service

# Create your views here.
class ServiceListView(ListView):
    template_name = 'services/service_list.html'
    queryset = Service.objects.all()
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    template_name = 'services/service_detail.html'
    queryset = Service.objects.all()
    context_object_name = 'service'


class ServiceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'services/service_create.html'
    queryset = Service.objects.all()
    form_class = ServiceModelForm

    def get_success_url(self):
        return reverse('services:servicespage')


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'services/service_update.html'
    queryset = Service.objects.all()
    form_class = ServiceModelForm

    def get_success_url(self):
        return reverse('services:servicespage')


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'services/service_delete.html'
    queryset = Service.objects.all()
    form_class = ServiceModelForm

    def get_success_url(self):
        return reverse('services:servicespage')