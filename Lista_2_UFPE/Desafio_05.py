piadas_boas = int(0)
piadas_ruins = int(0)
piada = str("")
reacao = str("")

while ((piada != "Fim do Show!")):
    piada = str(input())
    
    if (piada != "Fim do Show!"):
        reacao = str(input())

        if (reacao == "BAZINGA!"):
            piadas_boas += int(1)

        else:
            piadas_ruins += int(1)

else:

    total_reacoes = int(piadas_boas + piadas_ruins)

    if (piadas_boas > ((total_reacoes)*0.60)):
        print ("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")
    
    elif (piadas_ruins > (total_reacoes)*0.60):
        print ("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")

    else: 
        print ("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")