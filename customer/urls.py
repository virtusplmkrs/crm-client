from django.urls import path
from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

app_name = 'customer'

urlpatterns = [
    path('', CustomerCreateView.as_view(), name='customer-create'),
    path('list/', CustomerListView.as_view(), name='customer-list'),
    path('<int:id>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:id>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
]