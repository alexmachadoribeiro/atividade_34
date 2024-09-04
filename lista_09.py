eventos = []

while True:
    opcao = input('1 para cadastrar evento ou 2 para se inscrever: ')
    match opcao:
        case '1':
            evento = {}
            try:
                evento['nome'] = input('Informe o nome do evento: ')
                evento['censura'] = int(input('Informe a classificação indicativa do evento: '))
                eventos.append(evento)
                print('Evento cadastrado com sucesso.')
            except Exception as e:
                print(f'Não foi possível cadastrar evento. {e}.')
            finally:
                continue
        case '2':
            nome = input('Informe o seu nome: ')
            idade = int(input('Informe sua idade: '))
            while True:
                print(f'\n{'-'*30} EVENTOS {'-'*30}\n')
                for i in range(len(eventos)):
                    print(f'Código do evento: {i}')
                    for campo in eventos[i]:
                        print(f'{campo.capitalize()}: {eventos[i].get(campo)}.')
                    print('-'*30)
                try:
                    codigo_evento = int(input('Informe o código do evento: '))
                except Exception as e:
                    print(f'Não foi possível se inscrever para o evento. {e}.')
                finally:
                    break
            continue
        case _:
            print(f'Opção inválida.')
            break
            # TODO