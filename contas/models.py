from django.db import models
from django.conf import settings

from django.contrib.auth.models import update_last_login


from .constants import ESCOLHAS_GENERO, NAO_DECLARADO, ESTADOS


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	img = models.CharField(max_length=255,null=True)

	idade = models.IntegerField(null=True)
	genero = models.CharField(max_length=100, choices=ESCOLHAS_GENERO, null=True, default=NAO_DECLARADO)
	bio = models.CharField(max_length=500)
	profissao = models.CharField(max_length=255, null=True)

	logradouro = models.CharField(max_length=255, null=True)
	numero = models.CharField(max_length=50, null=True)
	cep = models.CharField(max_length=50, null=True)
	cidade = models.CharField(max_length=150, null=True)
	estado = models.CharField(max_length=80, choices=ESTADOS, null=True)