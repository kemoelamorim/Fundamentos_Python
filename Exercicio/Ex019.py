"""
Um professor quer sotear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice
alunos = []
for i in range(4):
    i = input("Digite o nome do aluno: ")
    alunos.append(i)

print(f"O aluno sorteado foi: {choice(alunos)}")