# WHILE = ENQUANTO

# O loop while em python é uma das formas mais comuns para executar iterção
# A instrução while sera executada repetidamente, seja uma única instrução ou grupo de intrução
  # desde que a condição seja verdadeira 


# Valida cada item em uma série de valores 
expressao1 = 0
while (expressao1):
    print ("comando executado caso a expressão1 seja verdadeira") # O loop para quando a expressão se torna falsa

#------------------------

# Usando o loop while para imprimir os valores de 0 a 9
counter = 0
while counter < 10:
    print(counter)   # ira executar até a expressão for falsa
    counter = counter + 1 # A cada loop é adicionado +1 para chegar até 10 e fechar o loop

#-------------------------

# Também é possível usar a claúsula else para encerrar o loop while
x = 0

while x < 10:
    print ('O valor de x nesta iteração é: ', x)
    print (' x ainda é menor que 10, somando 1 a x')
    x += 1
    
else:                              # No Python podemos utilizar o 'else' junto com o while
    print ('Loop concluído!')      # Aqui o else indica o fim do loop, quando a expressão da falsa 

#-------------------------

# Pass, Break, Continue
counter = 0
while counter < 100:
    if counter == 4:
        break              # O Break interrompe o loop quando o counter for igual a 4 
    else:
        pass
        print(counter)
    counter = counter + 1

#--------------------------

for verificador in "Python":
    if verificador == "h":
        continue           # neste caso esta verificando se tem o 'y' e o programa contionua rodando normal  
    print(verificador)


#--------------------------

for i in range(2,30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j = j + 1
        else:
            j = j + 1
    
    if counter == 0:
        print(str(i) + " é um número primo")
        counter = 0
    else:
        counter = 0