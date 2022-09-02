nome = str(input("Qual é o seu nome? "))
resp = int(0)

print (f"{nome}! Vamos fazer um teste")

numb = int(input("Digite um número para o teste: "))

while (numb <= int(0)):
    print (f"{nome}! Esse número não é permitido!")
    numb = int(input("Digite um número para o teste: "))

else:

    for i in range (1,(numb),1):

        if (i == (numb-1)): #essa estrutura é desnecessária, poderia fazer isso no else da linha 24, porém queria treinar o aninhamento.
            print (f"{i}² + {numb} =" , end="")
        
        else:
            print (f"{i}² + ", end= "")
        
        resp += (i**2)

    else:
        resp += (numb**2)
        print (f" {resp}")