from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    queryset = Product.objects.filter(inventory__lt=10)
    return render(request, 'hello.html', {'name': 'Lili', 'products': list(queryset)})
