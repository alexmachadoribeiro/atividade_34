'''
Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.
'''

numero = int(input('Informe um número: '))

print(f'{numero} é par.' if numero % 2 == 0 else f'{numero} é ímpar.')