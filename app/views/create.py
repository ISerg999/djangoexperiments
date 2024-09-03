from django.shortcuts import render
from django.http import HttpResponseRedirect

# from ..models.company import Company
# from ..models.product import Product


def create(request):
    # create_companies()
    if request.method == 'POST':
        # product = Product()
        # product.name = request.POST.get('name')
        # product.price = request.POST.get('price')
        # product.company_id = request.POST.get('company')
        # product.save()
        return HttpResponseRedirect("/")
    # companies = Company.objects.all()
    companies = []
    return render(request, "create.html", {"companies": companies})

# def create_companies():
#     if Company.objects.all().count() == 0:
#         Company.objects.create(name='Gigabyte')
#         Company.objects.create(name='Asus')
#         Company.objects.create(name='MSI')