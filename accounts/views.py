from django.shortcuts import render
from accounts.forms import UserLoginForm
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
