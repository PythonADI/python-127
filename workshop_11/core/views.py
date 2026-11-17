from django.shortcuts import render, get_object_or_404
from core.models import Product

def home_view(request):
    # how to get products from database +
    # in which HTML should we render this products +
    # print(request)
    # print(request.method)
    # print(request.GET)
    # print(request.GET.get("search"))
    products = Product.objects.all()
    
    for product in products:
        print(product.name)
    return render(
        request,
        "index.html", 
        {
            "products": products
        }
    )


def about_view(request):
    return render(request, "about.html")


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(
        request,
        "product_detail.html",
        {
            "product": product
        }
    )
