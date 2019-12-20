from django.shortcuts import render
from .models import Product, BaseProduct, Category
from django.utils import timezone


def index(request):
    """Render the index page"""
    new_products = Product.objects.filter(
        created_date__lte=timezone.now()).order_by("created_date")[:3]
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

    return render(request, "products.html", {
        "products": products, "motherboards": motherboards,
        "categories": category, "processors": processors,
        "graphics": graphics_cards
    })


def motherboards(request):
    """Render the products/motherboards page"""
    products = Product.objects.all()
    base_products = BaseProduct.objects.all()
    category = Category.objects.all()
    motherboards = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Motherboards").id))
    processors = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Processors").id))
    graphics_cards = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Graphics").id))

    return render(request, "products.html", {
        "products": motherboards,
        "motherboards": motherboards,
        "categories": category, "processors": processors,
        "graphics": graphics_cards
    })


def processors(request):
    """Render the products/processors page"""
    products = Product.objects.filter(baseproduct_id=3)
    base_products = BaseProduct.objects.all()
    category = Category.objects.all()
    motherboards = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Motherboards").id))
    processors = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Processors").id))
    graphics_cards = products.filter(baseproduct_id=base_products.get(
        category_id=category.get(name="Graphics").id))

    return render(request, "products.html", {
        "products": processors,
        "motherboards": motherboards,
        "categories": category, "processors": processors,
        "graphics": graphics_cards
    })


def graphics(request):
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

    return render(request, "products.html", {
        "products": graphics_cards,
        "motherboards": motherboards,
        "categories": category, "processors": processors,
        "graphics": graphics_cards
    })
