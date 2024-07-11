# Questão 01 - Laridsa...

print("Fim da questão 01")

############################################################################## 

#Questão 2 - Clara
print("Início da questão 02")
print("Este programa realiza a soma dos valores númericos inseridos pelo usuário. digite 0 para encerrar o programa e visualizar a soma")
soma=0
while True:
    a = float(input("digite um número ou 0 para sair:"))
    if a == 0 :  
        break  
    soma = soma + a
print("o resultado da soma é:", soma)
print("Fim da questão 02")


##############################################################################

#questão 03-lucimar
print("Início da questão 03")
senha_armazenada = "10"
senha_digitada = 1

while senha_digitada != senha_armazenada:
  # Continua pedindo a senha até que o usuário digite a senha correta
  senha_digitada = input("Digite sua senha: ")

  if senha_digitada != senha_armazenada:
    print("Senha incorreta. Tente novamente.")

print("Senha correta.")
print("Fim da questão 03")


##############################################################################
# Questão 05
n = int(input("Digite um valor inteiro positivo"))
i =1
fat=1
while i <= n:
    fat *= i
    i += 1
print ( "A fatorial do número escolhido é:",fat)

###############################################################################
# Questão 08
p = int( input("digite um número inteiro com 2 ou mais dígitos"))
soma=0
while p != 0:
    r = p % 10
    p = p // 10
    soma = soma + r
print( "A soma dos dígitos do número é ", soma)
print ("Fim do programa!")




