from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .Endereco import Endereco
from .Carrinho import Carrinho
from .Categoria import Categoria
from .Produto import Produto
from .ItemDeProduto import ItemDeProduto
from .Profile import Profile
from .Pedido import Pedido
from .Venda import Venda
from .Pagamento import Pagamento
from .Entrega import Entrega



