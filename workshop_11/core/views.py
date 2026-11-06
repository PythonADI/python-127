from django.shortcuts import render
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
