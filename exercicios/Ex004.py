""" 
Faça um programa que leia algo  pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
"""

tipo = input('Digite algo: ')
print(f'O tipo primitivo do valor digitado é: {type(tipo)}')
print('Só tem espaços?', tipo.isspace())
print('É um número?', tipo.isnumeric())
print('É alfabetico?', tipo.isalpha())
print('É alfanumrico?', tipo.isalnum())
print('Está em maiúscula?', tipo.isupper())
print('Está em minúscua?', tipo.islower())
print('Está capitalizada?', tipo.istitle())


