from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from app.models.company import Company
from app.models.product import Product


def edit(request, id):
    try:
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.company_id = request.POST.get('company')
            product.save()
            return HttpResponseRedirect('/')
        else:
            companies = Company.objects.all()
            return render(request, 'edit.html', {'product': product, 'companies': companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')
