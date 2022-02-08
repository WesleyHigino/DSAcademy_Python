# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia_da_semana = input("Escreva qual o dia da semana: ")
dia6 = "sabado"
dia7 = "domingo"

if dia_da_semana == dia6 or dia_da_semana == dia7:
    print("Hoje é dia de folga")
else:
    print("Voce precisa trabalhar")


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista


lista_frutas = ["banana", "laranja", "morango", "uva","abacate"]
if "morango" in lista_frutas:
    print("morango faz parte da lista")
else: 
    print("Não tem morango na lista")


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

elementos = (4,8,16,32)
lista1 = []

for i in elementos:
    mult = i * 2
    lista1.append(mult)

print(lista1)  
 

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 151, 2):
    print(i)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temperatura = 40

while (temperatura > 35):
    print(temperatura)
    temperatura = temperatura -1


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0
while contador < 100:
    print(contador)
    contador = contador +1
    if contador == 23:
        break




# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
lista2 =[]
valor1 = 4

for i in range (valor1,21,2):
    valor1 = valor1 +1
    lista2.append(i)
    print(lista2)



# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)

nums = range(5, 45, 2)
for i in nums:
    lista3 = []
    lista3.append(i)
    print(lista3)   #Duas formas de resolver o problema, 1 - especificando indice por indice da lista

print(list(nums)) # 2 - Apenas utilizando a função list 


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.

temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:                 #1 erro de sintaxe no if, faltando os dois pontos
    print('Vista roupas leves.')     #2 erro de indentação
else:                                #3 erro de sintaxe no else, faltando os dois pontos
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão.
# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)​

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir"
contador = 0
for caract in frase:
    if caract == 'r':
       contador += 1
print("A letra 'r' aparece %d vezes" %(contador))