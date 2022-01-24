print("Calculadora".upper)
print("--------------")

print("Digite o simbulo da operação que deseja realizar:")
print("")
print("Digite:")
print("'/' para Divisão ")
print("'*' para Multiplicação ")
print("'+' para Adição ")
print("'-' para Subtração ")
operação=input("Operação: ")

while op2 == "s" :  
 if (operação ==("/")):
  print("Digite dois digitos para divisão")
  numero1 = int(input())
  numero2 = int(input())
  resultado = numero1/numero2
  print("Resultado = " + str(resultado))

 elif (operação ==("*")):
  print("Digite dois digitos para Multiplicação")
  numero1 = int(input())
  numero2 = int(input())
  resultado = numero1*numero2
  print("Resultado = " + str(resultado))  

 elif (operação ==("+")):
  print("Digite dois digitos para adição")
  numero1 = int(input())
  numero2 = int(input())
  resultado = numero1+numero2
  print("Resultado = " + str(resultado))  

 elif (operação ==("-")):
  print("Digite dois digitos para Subtração")
  numero1 = int(input())
  numero2 = int(input())
  resultado = numero1-numero2
  print("Resultado = " + str(resultado))
       
 print("Digite 's' para voltar ao inicio ou 'n' para encerrar")
 op2 = input()