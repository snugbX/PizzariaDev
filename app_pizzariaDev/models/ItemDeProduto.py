from app_pizzariaDev.models import *
from app_pizzariaDev.models import Produto, Carrinho


class ItemDeProduto(models.Model):
	id_Produto = models.ForeignKey(Produto ,on_delete=models.CASCADE, null=False, blank=False)
	id_Carrinho = models.ForeignKey(Carrinho ,on_delete=models.CASCADE, null=False, blank=False)
	data_Fabricacao = models.DateField(null=True, blank=True)
	validade = models.DateField(null=True, blank=True)
	preco_Atualizado = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)

	def __str__(self):
		return self.id_Produto