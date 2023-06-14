from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
# permite usar o operador or na estrutura de desição.
from django.db.models import Q


# Create your views here.
class CustomerListView(ListView):
    # chama esse templates
    template_name = 'customer/customer-list.html'
    # referente a paginação da pagina customer-list.html (Faça alguns condicionamentos para tratar os erros)
    paginate_by = 5
    # consome o conteudo a partir da models
    model = Customer
    # executa uma consulta a partir da models
    #queryset = Customer.objects.all()
    # executa uma consulta a partir da bara de pesquisa

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )
        else:
            object_list = Customer.objects.all()
        return object_list
    
        
class CustomerCreateView(CreateView):
    template_name = 'customer/customer.html'
    # faz uso do formulario do Django
    form_class = CustomerForm

    # função para validar o formulario do Django
    def form_valid(self, form):
        return super().form_valid(form)

    # função para direcionar a pagina apos ser salvo o registro do Django
    def get_success_url(self):
        return reverse('customer:customer-list')

class CustomerUpdateView(UpdateView):
    template_name = 'customer/customer.html'
    # faz uso do formulario do Django
    form_class = CustomerForm

    # busca o registro (objeto) ao qual foi clicado (query)
    def get_object(self):
        id = self.kwargs.get('id')
        #Customer.objects.get(id=id) # sem tratativa de erro
        return get_object_or_404(Customer, id=id) # com tratativa de erro

    # função para validar o formulario do Django
    def form_valid(self, form):
        return super().form_valid(form)

    # função para direcionar a pagina apos ser salvo o registro do Django
    def get_success_url(self):
        return reverse('customer:customer-list')

class CustomerDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get('id')
        #Customer.objects.get(id=id) # sem tratativa de erro
        return get_object_or_404(Customer, id=id) # com tratativa de erro

    def get_success_url(self):
        return reverse('customer:customer-list')