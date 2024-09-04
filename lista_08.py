'''
Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.
'''

import os

notas = []

while True:
    opcao = input('1 para inserir nota ou 2 para calcular média: ')
    os.system('cls')
    match opcao:
        case '1':
            try:
                nova_nota = float(input('Informe um valor de 0 a 10: ').replace(',','.'))
                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print('Nota inserida com sucesso.')
                else:
                    print('Nota inválida.')
            except Exception as e:
                print(f'Não foi possível inserir a nota. {e}.')
            finally:
                continue
        case '2':
            break
        case _:
            print('Opção inválida.')
            continue

print(f'Média: {(sum(notas)/len(notas)):,.2f}')