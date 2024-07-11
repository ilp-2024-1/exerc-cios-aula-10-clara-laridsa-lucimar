# Questão 01 - Laridsa...
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


##############################################################################
# Questão 05
n = int(input(" digite um valor inteiro positivo"))
i =1
fat=1
while i <= n:
    fat *= i
    i += 1
print ( "a fatorial do número escolhido é:",fat)

###############################################################################
# Questão 08
p = int( input("digite um número inteiro com 2 ou mais dígitos"))
soma=0
while p != 0:
    r = p % 10
    p = p // 10
    soma = soma + r
print( " a soma dos dígitos do número é ", soma)
print ("fim do programa!")





