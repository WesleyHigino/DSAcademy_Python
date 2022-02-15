# Métodos são essencialmente funções incorporadas em objetos.and
# Métodos permitem executar ações especificas no objeto e podem também ter argumetos, exatamente como uma função

# sintaxe:
# objeto.método(arg1, arg2, etc...)

# Exemplo de métodos:
# metodos para objeto lista:
# append
# count 
# extend 
# insert 
# pop 
# remove 
# reverse 
# sort 

# Criando uma lista
lst = [100, -2, 12, 65, 0]

# Usando um método do objeto lista
print(lst.append(10)) # permitite adicionar um elemento a lista 

# Imprimindo a lista
print(lst)

# Usando um método do objeto lista
print(lst.count(10))

# A função help() explica como utilizar cada método de um objeto
print(help(lst.count))

# A função dir() mostra todos os métodos e atributos de um objeto
print(dir(lst)) # mostra os atributos e os metodos 

# O método de um objeto pode ser chamado dentro de uma função, como print()

a = 'Isso é uma string'
print (a.split()) # O método sempre tem o abra e fecha parenteses 


listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)