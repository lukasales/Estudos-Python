nome = str(input("Qual é seu nome? "))

resp = str(input("Vamos fazer uma conta? "))

while (resp != "Sim" and resp != "Não"):
    print ("Esse valor não é permitido")
    resp = str(input("Vamos fazer uma conta? "))

    if (resp == "Não"):
        print (f"{nome}! Certo, que pena")
    
else: 
    print (f"{nome}! Que bom, vamos lá!")

    x = float(input("Escolha um valor: "))
    y = float(input("Escolha outro valor: "))

    while ((x == 0 and x > 1) and (y == 0 and y > 1)):
        print ("Valores não permitidos, escolha números entre 0 à 1")

    else:

        z = int(2)
        w = int(3)
        s = (x*y)
        soma = (s)

        while (soma > 0.001):
            soma += ((x**z*y**w)/(x+y)**(z*w))
            soma *= (-1)
            s += (soma)
            z += int(1)
            w += int(2)

        else:  
            print ("Fim da conta")