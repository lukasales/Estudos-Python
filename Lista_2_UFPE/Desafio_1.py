N = int(input())
pontos_sheldon = int(0)
pontos_raj = int(0)


while (N > 0):
    #aqui eu faço a estrutura do jogo e sempre subtraiu uma unidade de N
    escolha_sheldon = str(input())
    escolha_raj = str(input())

    if ((escolha_sheldon == "lagarto")):

        if ((escolha_raj == "spock")):
            pontos_sheldon += int(1)

        elif ((escolha_raj == "tesoura")):
            pontos_raj += int(1)
        
    elif ((escolha_sheldon == "spock")):

        if ((escolha_raj == "tesoura")):
            pontos_sheldon += int(1)
        
        elif ((escolha_raj == "lagarto")):
            pontos_raj += int(1)
        
    elif ((escolha_sheldon == "tesoura")):

        if ((escolha_raj == "lagarto")):
            pontos_sheldon += int(1)

        elif ((escolha_raj == "spock")):
            pontos_raj += int(1)
    
    elif((escolha_sheldon == escolha_raj)):
        pontos_sheldon += int(0)
        pontos_raj += int(0)

    N -= int(1)

else: 

    if (pontos_sheldon > pontos_raj):
        print ("BAZINGA! EU SOU O SENHOR DA SALA!")
    
    elif (pontos_sheldon == pontos_raj):
        print ("Oh não, precisamos de outra rodada.")
    
    elif (pontos_sheldon < pontos_raj):
        print ("ENGOLE ESSA, SHELDON!")