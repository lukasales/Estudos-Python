N = int(input())
melhor_planeta = int(0)

while ( N < int(2)):

    print ("Número inválido, tente novamente")
    N = int(input())

else:

    for i in range (0,N,1):
        nome = str(input())
        raio = float(input())
        massa = float(input())
        temperatura = float(input())

        IH = ((raio + massa + (temperatura/288))/3)
        resultado = abs(IH)

        if (abs(1 - resultado) < abs(1 - melhor_planeta)):
            melhor_planeta = (resultado)
            nome_melhor_planeta = (nome)
        
    else:

        if (melhor_planeta == int(1)):
            print (f"{nome_melhor_planeta} é perfeito!")

        elif (melhor_planeta < int(1)):
            print (f"{nome_melhor_planeta} vai dar pro gasto")
                
        else:
            print (f"{nome_melhor_planeta} vai ter que servir")