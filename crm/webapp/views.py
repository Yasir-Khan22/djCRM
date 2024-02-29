from django.shortcuts import render, redirect
# Create your views here.
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

# Home page 
def home(request):
    return render(request, "webapp/index.html")

# def index(request):
#     return render(request, "webapp/base.html")

# Register Page
# Register a User  
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    # return redirect()
    context = {'form': form}
    return render(request, "webapp/register.html", context=context)



def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            #return redirect(" ")

    context = {'form': form}
    return render(request, 'webapp/login.html',  context=context)