import os
import time

numero = int(input('Informe um número inteiro positivo: '))

os.system('cls')

print('Contagem regressiva:')

for i in range(numero, -1, -1):
    print(f'{i}...')
    time.sleep(1)
    os.system('cls')