from django.shortcuts import render

from app.models.product import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
