from app_pizzariaDev.models import *
from app_pizzariaDev.constantes import FORMA_PAGAMENTO


class Pagamento(models.Model):
	forma = models.CharField(max_length=4, choices=FORMA_PAGAMENTO, default='pix')
	id_Venda = models.ForeignKey(Venda, on_delete=models.CASCADE, null=False, blank=False)
