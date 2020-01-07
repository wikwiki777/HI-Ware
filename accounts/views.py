from django.shortcuts import render, redirect, reverse
from accounts.forms import UserLoginForm, UserRegistrationForm, ShippingDetailsForm
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def login(request):
    """Return a login page."""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST['password']
            user = auth.authenticate(request,
                                     username=username,
                                     password=password)

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are logged in")
            else:
                messages.error(request, "Incorrect Username or Password.")
# Consider usage for more descriptive feedback to user
# login_form.add_error("password", "Incorrect Username Password combination")

    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})


def registration(request):
    """Render the registration page."""

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, "You have succssfully registered")

    else:
        registration_form = UserRegistrationForm()

    return render(request, "registration.html",
                  {"registration_form": registration_form})


def profile(request):
    """Render the profile page"""
    user = User.objects.get(email=request.user.email)

    # update shipping information
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=request.user)
        shipping_form = ShippingDetailsForm(
            request.POST, instance=request.user.shippingdetails)
        if shipping_form.is_valid():
            shipping_form.save()
            messages.success(request, 'Your profile was successfully updated')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserRegistrationForm(instance=request.user)
        shipping_form = ShippingDetailsForm(
            instance=request.user.shippingdetails)

    return render(request, "profile.html", {"profile": user,
                                            "user_form": user_form, "shipping_form": shipping_form})


def logout(request):
    """Log the user out and redirect."""
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out!')
    return redirect(reverse('login'))
