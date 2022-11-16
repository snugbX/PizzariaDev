ESTADOS = (
	("Acre", "AC"),
	("Alagoas", "AL"),
	("Amapá", "AP"),
	("Amazonas", "AM"),
	("Bahia", "BA"),
	("Distrito Federal", "DF"),
	("Espírito Santo", "ES"),
	("Goiás", "GO"),
	("Maranhão", "MA"),
	("Mato Grosso", "MT"),
	("Mato Grosso do Sul", "MS"),
	("Minas Gerais", "MG"),
	("Pará", "PA"),
	("Paraíba", "PB"),
	("Paraná", "PR"),
	("Pernambuco" , "PE"),	
	("Piauí", "PI"),
	("Rio de Janeiro", "RJ"),
	("Rio Grande do Norte", "RN"),
	("Rio Grande do Sul", "RS"),
	("Rondônia", "RO"),
	("Roraima", "RR"),
	("Santa Catarina" , "SC"),
	("São Paulo", "SP"),
	("Sergipe", "SE"),
	("Tocantins", "TO"),
)

ROLE_CHOICE = (
	(1,'Admin'),
	(2,'Cliente')
)

STATUS_VENDA = (
	('F', 'Finalizada'),
	('C', 'Cancelada'),
	('E', 'Em Andamento')
)

STATUS_ENTREGA = (
	('F', 'Finalizada'),
	('C', 'Cancelada'),
	('E', 'Em Andamento'),
	('P', 'Parada')
)

FORMA_PAGAMENTO = (
	('pix','PIX'),
	('car','Cartao'),
	('din','Dinheiro')
)