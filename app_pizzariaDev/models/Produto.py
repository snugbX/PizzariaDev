from app_pizzariaDev.models import *

class Produto(models.Model):
	nome = models.CharField(max_length=150, null=False, blank=False)
	descricao = models.CharField(max_length=255, null=False, blank=False)
	preco = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)
	id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)
	img = models.CharField(max_length=255, null=False, blank=False)


	def __str__(self):
		return self.nome