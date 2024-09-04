'''
Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.
'''

peso = float(input('Informe o peso do bebê em gramas: '))

print('O bebê está liberado.' if peso >= 2500 else 'O bebê precisa ser internado.')