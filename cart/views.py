from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """Render the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of items to the cart"""
    quantity = int(request.POST.get("quantity"))

    cart = request.session.get("cart", {})
    cart[id] = cart.get(id, quantity)

    request.session["cart"] = cart
    return redirect(reverse("products"))


def adjust_cart(request, id):
    """Adjust the quantity of items in the cart"""
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(str(id))

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))
