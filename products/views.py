from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from products.forms import ProductForm

from products.models import Product

# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1>Hello, welcome</h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, "product-detail.html", {"product": product})


def get_products(request):
    products = Product.objects.all()
    new_products = []
    for product in products:
        prod = {
            "name": product.name,
            "descripion": product.description,
            "price": product.price,
        }

        new_products.append(prod)

    context = {"products": new_products}
    print(context)
    return render(request, "product-list.html", context)


def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    context = {"form": form}
    return render(request, 'product-create.html', context)