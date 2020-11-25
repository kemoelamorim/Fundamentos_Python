"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
# entrada
km_rodados = float(input("Digite a quantidade de Km rodados: "))
dias_alugados = int(input("Quantos dias? "))

# processamento 
pagar_diaria = dias_alugados * 60
pagar_km = 0.15 * km_rodados
total = pagar_diaria + pagar_km

# saída
print("Total a pagar R${:.2f}".format(total))