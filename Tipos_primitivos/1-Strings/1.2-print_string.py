# imprimindo um texto direto com função print()
print('aspas simples permite aspas "duplas" incorporadas \n') # \n quebra a linha da string

print("aspas duplas permite aspas 'simples' incorporadas \n")

print("""Texto com quebra de linha sao 
Strings entre aspas triplas podem ocupar várias linhas - 
todos os espaços em branco associados serão incluídos no literal da string.
""")

# Cuidados na quebrando linha
# print('\local\nome') separando com \n
print(r'\local\nome') # anulando \n

# end =('texto', valores) incrementa no final
finaldaFrase = ' desta frase'
print("inserindo algo no final", end = finaldaFrase ) 
