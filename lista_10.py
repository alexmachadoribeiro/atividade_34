'''
Crie um programa em que o usuário cadastre quantos cursos ele quiser (nome do curso, duração do curso em horas, Período do dia, quantidade de vagas) e exiba na tela.
'''

import os

cursos = []

while True:
    opcao = input('1 para cadastrar novo curso ou 2 para exibir a lista de cursos cadastrados: ')
    os.system('cls')
    match opcao:
        case '1':
            curso = {}
            try:
                curso['Nome'] = input('Informe o nome do curso: ').capitalize()
                curso['Duração do curso'] = int(input('Informe a duração do curso: '))
                curso['Período'] = input('Matituino, Vespertino ou Noturno: ').lower()
                curso['Vagas'] = int(input('Informe o número de vagas: '))
                cursos.append(curso)
                print('Curso cadastrado com sucesso.')
            except Exception as e:
                print(f'Não foi possível cadastrar novo curso. {e}.')
            finally:
                continue
        case '2':
            for curso in cursos:
                for campo in curso:
                    print(f'{campo}: {curso.get(campo)}.')
                print('-'*30)
            break
        case _:
            print('Opção inválida.')
            continue