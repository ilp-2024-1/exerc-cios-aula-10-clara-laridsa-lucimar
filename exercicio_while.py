# Questão 01 - Laridsa...
from http.client import OK


variavel = int (input("Digite um número de 1 a 100: "))
# numero  1 >= 100 
while (variavel >= 1 and variavel <=100):
    print("O número digital está dentro do intervalo entre 1 e 100.")
    variavel = int (input("Digite um número de 1 a 100: "))

print("Fim da questão 01")

############################################################################## 

#Questão 2 - Clara
print(" este programa realiza a soma dos valores númericos inseridos pelo usuário. digite 0 para encerrar o programa e visualizar a soma")
soma=0
while True:
    a = float(input("digite um número ou 0 para sair:"))
    if a == 0 :  
        break  
    soma = soma + a
print("o resultado da soma é:", soma)
print("fim do programa")

######### Questão 04 - Laridsa... #########################################################################
print(input("Dê um palpite:"))
palpite = range(1,100)
total_de_tentativas = variavel
print(palpite)
while (palpite +100):
      print(input("tentativa"))
print("você digitou")

if (palpite <1 or palpite >100):
 print("voce deve escolher um número entre 1  e 100")

if palpite == 35:
    print("você acertou!")
else:
   
 print("fim !")




            
    




