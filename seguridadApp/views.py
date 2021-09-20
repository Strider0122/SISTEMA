from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def acceder(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario= authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                login(request,usuario)
                return redirect("home")
            else:
                messages.error(request,"Los datos son incorrectos")
        else:
            messages.error(request,"Los datos son incorrectos")
            
    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})
@login_required(login_url="login")
def home(request):  
    return render(request,"home.html")
@login_required(login_url="login")
def salir(request):
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login")