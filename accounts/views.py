from django.shortcuts import render
from accounts.forms import UserLoginForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.exceptions import ObjectDoesNotExist



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

            try:
                User.objects.get(username=username)
                user_exist = True
            except ObjectDoesNotExist:
                user_exist = False
                login_form.add_error("username", "Username does not exist")

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are logged in")
            elif user_exist:
                login_form.add_error("password", "Incorrect Password")

    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})
