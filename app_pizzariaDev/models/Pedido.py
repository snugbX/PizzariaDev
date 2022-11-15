from app_pizzariaDev.models import *
from django.conf import settings

class Pedido(models.Model):
	id_Carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, null=False, blank=False)
	id_User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
	id_Endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False, blank=False)
	preco_Total = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)
