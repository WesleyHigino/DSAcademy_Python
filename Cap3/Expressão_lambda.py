# Definindo uma função - 3 linhas de código
def potencia(num):
    result = num**2  
    return print(result)

potencia(5)

# Definindo uma função - 2 linhas de código
def potencia(num):
    return print(num**2)  

potencia(10)

# Definindo uma função - 1 linha de código
def potencia(num): return  print(num**2) 
potencia(4)

#-------------------------------
# Definindo uma expressão lambda
# ------------------------------

# É uma função anonima

potencia = lambda num: print(num**2)
potencia(7)

# Lembre: operadores de comparação retornam boolean, true or false
par = lambda x: print(x%2==0) # esta verificando se x dividivo por dois é igual a zero
par(2)
par(4)

first = lambda s: print(s[0]) # Busca o indice referente a posição informada da string
first("wesley")

reverso = lambda s: print(s[::-1]) # '-1' tras o caracter a partir do final, ':' retira a ultima letra, '::' inverte a ordem das letras 
reverso("wesley")

addNum = lambda x,y : x+y #busca dois valores
addNum(2,4)
