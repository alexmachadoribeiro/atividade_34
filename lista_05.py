nomes = ['Alex', 'Alexandre', 'Fulano', 'Cicrano', 'Beltrano', 'Alexandra', 'Joana', 'Maria', 'José', 'João']
indice = int(input('Informe um índice: '))

print(nomes[indice] if indice >= 0 and indice < 10 else 'Índice inexistente.')