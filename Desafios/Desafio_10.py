nome = str(input("Qual é o seu nome? "))

numb = int(input("Digite um número? "))
fatorial = int(1)

while (numb <= int(0)):
    print ("Esse número não é permitido, {nome}! \nPor favor! digite um número maior que zero!")
    numb = int(print("Digite um número? "))

else:
    for i in range (1, numb, 1):
        fatorial *= (i)
    
    if (fatorial == int(0)):
        print (f"{nome}! O fatorial de {numb} é igual a 1")

    else:
        fatorial *= int(numb)
        print (f"{nome}! O fatorial de {numb} é a {fatorial}")