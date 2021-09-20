from django.urls import path
from .views import acceder,home,salir
urlpatterns = [
    path('login/',acceder,name="login"),
    path('home/',home,name="home"),
    path('logout/',salir,name="logout"),

]