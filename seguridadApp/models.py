from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    tipo = models.CharField(max_length=15,default='administrador',null=True)
