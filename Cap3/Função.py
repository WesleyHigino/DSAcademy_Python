# Utilizando função
def primeiafunc():
    print("fala fiote")

primeiafunc() # chamando a função


def segunfunc(nome):
    print("hello %s" %(nome))

segunfunc("aluno")

def tercefunc():
    for i in range(0,5):
        print("Numero "+ str(i))

tercefunc()

def addnum(primeiro,segundo):
    print("primeiro número: " + str(primeiro))
    print("segundo numero: " + str(segundo))
    print("Soma: ", primeiro + segundo)

# chamando a função e chamando os parametros
addnum(45,50)

# ------------------------------
# Variável Global
var_global = 10  # Esta é uma variável global

def multiply(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiply(50,40)
print(var_global)

# Variável Local
var_global = 10  # Esta é uma variável global
def multiply(num1, num2):
    var_local = num1 * num2   # Esta é uma variável local
    print(var_local)

multiply(5,25)
#-----------------------------------
#Funções Built-in
print(abs(-50)) # deixa valor positivo
print(abs(23))

print(bool(0)) #retorna false quando a função é zero
print(bool(1))

# -----------------------------------
# Funções str, int, float

# Erro ao executar por causa da conversão, UTILIZAR O INT NO INPUT
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar o Facebook")  


int("26")

float("123.345")

len([23,34,45,46])

array = ['a', 'b', 'c']
print(max(array))
print(min(array))

array = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
print(array)

list1 = [23, 23, 34, 45]
print(sum(list1))

# --------------------------------------
# Fazendo split dos dados

import math
'''verifica se um numero é primo
'''
def numPrimo(num):
    if num % 2 == 0 and num >2:
      return print("este numero não é primo")
    for i in range(3, int(math.sqrt(num)) +1,2):
        if num % i == 0 :
            return print("este numero não é primo" )
    return print("este numero é primo")            

numPrimo(541)

# Fazendo split dos dados

def split_string(text):
    return print(text.split(" "))
texto = "Esta função será bastante útil para separar grandes volumes de dados."

# Podemos atribuir o output de uma função, para uma variável
token = split_string(texto)
print(token)

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"
def lowercase(text):
    return print(text.lower())


# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ): # o * permite colocar quantos parametros quiser
   # Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return

# Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10) # um parametro

printVarInfo('Chocolate', 'Morango', 'Banana') # três parametros 