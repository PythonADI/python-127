from django.shortcuts import render, get_object_or_404
from core.models import Product

def home_view(request):
    # how to get products from database +
    # in which HTML should we render this products +
    # print(request)
    # print(request.method)
    # print(request.GET)
    # print(request.GET.get("search"))
    q = request.GET.get("q")
    start_date = request.GET.get("start")
    end_date = request.GET.get("end")

    if q:
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.all()
        
    if start_date and end_date:
        products = products.filter(expiry_date__gte=start_date, expiry_date__lte=end_date)

    return render(
        request,
        "index.html", 
        {
            "products": products,
        }
    )


def about_view(request):
    return render(request, "about.html")


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(
        request,
        "product_detail.html",
        {
            "product": product
        }
    )
