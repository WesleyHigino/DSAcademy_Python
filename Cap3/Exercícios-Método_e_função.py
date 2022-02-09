# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e
# depois faça uma chamada à função para listar os número

from ast import arg


def sequence():
   for i in range(2,21,2):
    print(i)

sequence()    

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def text(nome):
    print("String : %s" %(nome.upper()))
    
text("wesley")

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista

def listafunc(lista):
    lista.append(14)
    lista.append(16)

lista1 =[4,8,10,12]
listafunc(lista1)
print(lista1)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def argum(arg1, *arg2):
    print(arg1)
    for i in arg2:
        print(i)
    
argum("wesley")
argum("w","e","s","l","e","y")



# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2
# números como parâmetro e retornar a soma deles
soma = lambda x,y: x+y 
print(soma(5,5))

       
# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local

total = 0

def soma( arg1, arg2 ):
    total = arg1 + arg2
    print ("Dentro da função o total é: ", total)
    return total
    
soma( 10, 20 )
print ("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!

Celsius = [39.2, 36.5, 37.3, 37.8]

Fahrenheit = map(lambda formul : (float(9)/5)*formul +32, Celsius)
print (list(Fahrenheit))

# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário

dic = {'k1': 'Natal', 'k2': 'Recife'}
dir(dic)

# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.

import pandas as pd 
print(dir(pd))

# ************* Desafio ************* (pesquise na documentação Python)
# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
import pandas as pd

file_name = "binary.csv"

def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()
    
retornaArq(file_name)  


