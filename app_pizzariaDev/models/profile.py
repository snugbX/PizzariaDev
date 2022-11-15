from app_pizzariaDev.models import *
from app_pizzariaDev.constantes import ROLE_CHOICE
from django.conf import settings

class Profile(models.Model):
	
	# Modelo que estende da estratégia de user profile, o usuario default do DJANGO

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	role = models.IntegerField(choices=ROLE_CHOICE, default=2)

	id_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False, blank=False)
	
