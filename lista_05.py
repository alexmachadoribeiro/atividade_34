'''
Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.
'''

nomes = ['Alex', 'Alexandre', 'Fulano', 'Cicrano', 'Beltrano', 'Alexandra', 'Joana', 'Maria', 'José', 'João']
indice = int(input('Informe um índice: '))

print(nomes[indice] if indice >= 0 and indice < 10 else 'Índice inexistente.')