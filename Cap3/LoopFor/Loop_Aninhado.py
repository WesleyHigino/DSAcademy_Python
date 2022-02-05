"""LOOP ANINHADO"""

# É muito comum para manipular matrizes

# Operando os valores de uma lista com loop for

listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2 # vai multiplicar o item por dois 
    soma += double_i  # += vai multiplicar cada item e fazer a soma das multiplicações 

print(soma)

#---------------------------

# Loops em lista de listas
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
for valor in listas:
    print(valor)
    print(valor[0]) # indice 0 de cada conjunto 

#---------------------------

# Contando os itens de uma lista
lista = [5,6,10,13,17]
count = 0
for item in lista:
    count += 1        # contando quantos elementos tem na lista
    
print(count)

#---------------------------

# Contando o número de colunas
lst = [[1,2,3],[3,4,5],[5,6,7]]
primeira_linha = lst[0]
count = 0
for column in primeira_linha:
    count = count + 1            # a cada validação do for se conta +1 item
    
print(count)

#---------------------------

# Pesquisando em listas
listaC = [5, 6, 7, 10, 50]

# Loop através da lista
for item in listaC:
    if item == 5:
        print("Número encontrado na lista!")

#---------------------------

# Listando as chaves de um dicionário
dict = {'k1':'Python','k2':'R','k3':'Scala'}
for item in dict:
    print(item)

# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
for k,v in dict.items(): # dict.items() função do dicionario 
    print (k,v)   # O 'k' e o 'v' representam chave e valor do dicionario 
