from app_pizzariaDev.models import*


class Carrinho(models.Model):
	data_criacao = models.DateTimeField(auto_now_add= True )
	data_Compra = models.DateTimeField(auto_now= True )

	def __str__(self):
		return self.data_criacao