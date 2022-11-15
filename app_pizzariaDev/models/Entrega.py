from app_pizzariaDev.models import *
from app_pizzariaDev.constantes import STATUS_ENTREGA


class Entrega(models.Model):
	id_Venda = models.ForeignKey(Venda, on_delete=models.CASCADE, null=False, blank=False)
	status_Entrega = models.CharField(max_length=4, choices=STATUS_ENTREGA, default='E')
	data_Envio = models.DateField(null=True, blank=True)
	data_Chegada = models.DateField(null=True, blank=True)