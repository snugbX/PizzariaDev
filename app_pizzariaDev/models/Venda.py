from app_pizzariaDev.models import *
from app_pizzariaDev.constantes import STATUS_VENDA

class Venda(models.Model):
	id_Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False, blank=False)
	data_Venda =  models.DateTimeField(auto_now_add= True )
	status = models.CharField(max_length=4, choices=STATUS_VENDA, default='E')
	preco_Total_Venda = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)