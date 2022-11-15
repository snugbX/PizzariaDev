from app_pizzariaDev.models import *
from app_pizzariaDev.constantes import ESTADOS

class Endereco(models.Model):
	logradouro = models.CharField(max_length=255, null=True)
	numero = models.CharField(max_length=255, null=True)
	cep = models.CharField(max_length=255, null=True)
	cidade = models.CharField(max_length=255, null=True)
	estado = models.CharField(max_length=255, choices=ESTADOS)

	def __str__(self):
		return self.logradouro