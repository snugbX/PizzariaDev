from app_pizzariaDev.models import *

class Categoria(models.Model):
	nome = models.CharField(max_length=150, null=False, blank=False)

	def __str__(self):
		return self.nome