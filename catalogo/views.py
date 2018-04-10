from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto
# Create your views here.
class ProductoListView(ListView):
    model = Producto