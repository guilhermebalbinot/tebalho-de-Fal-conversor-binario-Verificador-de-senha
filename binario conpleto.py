


import math

resultado = ''
n = float(input('digite o valor a ser trans formado em numero binario:'))
x = n
while n > 0:#o codigo vai ser repetetir do enquanto 'n' for maior que '0' 
##    n = n / 2    #'n' asumira o valor da divisão
  if n % 2 == 0: # 'n' vai ser dividido pro dois, só o resto da divisão vai ser conputado diferente de zero
    n = n / 2#'n' asumira o valor do resto da divisão
    resultado = '0' + str(resultado)
  else:
    n = n / 2#'n' asumira o valor da divisão
    n = math.floor(n)# o math.floor retorna o valor de 'x'
    resultado = '1' + str(resultado)

resultado = str(str('o valor de: ') + str(x)) + ('O numero em  binario:') + str(resultado)
print(resultado)




