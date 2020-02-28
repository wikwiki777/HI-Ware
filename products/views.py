from django.shortcuts import render
from .models import Product, BaseProduct, Category
from django.utils import timezone
from django.contrib.postgres.search import SearchVector


def index(request):
    """Render the index page"""
    new_products = Product.objects.all().order_by("-created_date")[:3]
    return render(request, "index.html", {"new_products": new_products})


def products(request):
    """Render the products page"""
    products = Product.objects.all()
    base_products = BaseProduct.objects.all()
    category = Category.objects.all()
    motherboards = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Motherboards").id))
    processors = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Processors").id))
    graphics_cards = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Graphics").id))

    if "motherboards" in request.path:
        return render(request, "products.html", {
            "products": motherboards,
            "motherboards": motherboards,
            "categories": category, "processors": processors,
            "graphics": graphics_cards
        })

    if "processors" in request.path:
        return render(request, "products.html", {
            "products": processors,
            "motherboards": motherboards,
            "categories": category, "processors": processors,
            "graphics": graphics_cards
        })

    if "graphics" in request.path:
        return render(request, "products.html", {
            "products": graphics_cards,
            "motherboards": motherboards,
            "categories": category, "processors": processors,
            "graphics": graphics_cards
        })

    return render(request, "products.html", {
        "products": products, "motherboards": motherboards,
        "categories": category, "processors": processors,
        "graphics": graphics_cards
    })


def product_details(request, id):
    """Render the products detail page"""
    product = Product.objects.get(pk=id)

    return render(request, "product_details.html", {
        "product": product
    })


def search_all(request):
    """Render the search results page"""
    products = Product.objects.annotate(search=SearchVector('brand', 'model', 'description')).filter(search=request.GET['search'])
    return render(request, "products.html", {"products": products})
