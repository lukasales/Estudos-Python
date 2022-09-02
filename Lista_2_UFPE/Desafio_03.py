X = int(input())

Y = int(0)
chave = False
pontos = int(0)

while (chave == False):

    Y = int(input())

    if(Y < int(0)):
        chave = True

    else:

        for i in range (1,Y,1):
            pontos += int(i)
            print (pontos)

        else: 
            pontos += int(Y)
            print (pontos)

else: 

    if (pontos < X):
        print ("Ainda falta um pouco...")

    elif (pontos == X):
        print ("Parabéns!!! Você é o mais inteligente")
    
    elif ((pontos > X) and (pontos < (X * 20))):
        print ("Parece que o gêniozinho passou um pouco do local...")
    
    elif ((pontos > (X * 20)) and (pontos <= (X * 100))):
        print ("Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?")
    
    elif ((pontos > (X * 100))):
        print ("Hum... acho que o gêniozinho não tem mesmo doutorado ein...")