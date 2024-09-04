'''
Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.
'''

import os

nomes = []

while True:
    novo_nome = input('Informe o novo nome ou deixe em branco para encerrar: ')
    os.system('cls')
    if novo_nome != '':
        try:
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.')
        except Exception as e:
            print(f'Não foi possível inserir o nome. {e}.')
        finally:
            continue
    else:
        break

nomes.sort()

print(f'Número de nomes na lista: {len(nomes)}.')
for nome in nomes:
    print(nome)