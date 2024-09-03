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
                for evento in eventos:
                    for campo in evento:
                        print(f'{campo.capitalize()}: {evento.get(campo)}.')
                    print('-'*30)
            # TODO