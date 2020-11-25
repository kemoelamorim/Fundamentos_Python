# Calcula raiz 
numero = int(input('Digite um numero para extrair a raiz: '))
raiz = int(input('Digite 2 para raiz quadrada, ou 3 para raiz cubica: '))
resultado = int(numero ** (1/raiz))

if raiz == 2:
  print(f"O número ({numero}) com a raiz Quadrada({raiz}) é igual a: {resultado}")
else:
   print(f"O número ({numero}) com a raiz Cubica({raiz}) é igual a: {resultado}")
#Outros operadores bitwise http://wiki.python.org/moin/BitwiseOperators