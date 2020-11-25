"""
Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15 % de aumento.
"""
# lendo um salário
salario = float(input("Digite o salário: "))

# novo salário
aumento = salario * 15/100
novo_salario = salario + aumento

# saída 
print(f"Salário {salario} com aumeto de {aumento}, com o total de {novo_salario} ")