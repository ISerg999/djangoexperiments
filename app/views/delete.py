from django.http import HttpResponseRedirect, HttpResponseNotFound

from app.models.product import Product


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')
