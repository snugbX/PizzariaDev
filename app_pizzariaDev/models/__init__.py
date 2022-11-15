from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from .Carrinho import Carrinho
from .Categoria import Categoria
from .Endereco import Endereco
from .Produto import Produto
from .ItemDeProduto import ItemDeProduto
from .Profile import Profile



