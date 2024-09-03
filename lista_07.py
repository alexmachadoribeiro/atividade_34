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

for nome in nomes:
    print(nome)