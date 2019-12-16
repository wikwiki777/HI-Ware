from django.shortcuts import render
from .models import Product
from django.utils import timezone


def index(request):
    """Render the index page"""
    new_products = Product.objects.filter(
        created_date__lte=timezone.now()).order_by("created_date")[:3]
    return render(request, "index.html", {"new_products": new_products})
