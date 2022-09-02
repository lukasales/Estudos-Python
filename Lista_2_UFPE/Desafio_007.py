mensagem = str(input())
passo_1 = False
passo_2 = False
passo_3 = False
passo_4 = False
passo_5 = False
nobel = False

while (mensagem != str("É o fim da Estrada pra Sheldon Cooper") and (nobel == False)):

    if (mensagem == str("Começou a Trabalhar na Caltech")):
        passo_1 = True
        mensagem = str(input())

        if ((mensagem == str("Bazinga"))):
            passo_1 = False
            mensagem = str(input())

    elif (mensagem == str("Trabalho sobre a String Theory") and (passo_1 == True)):
        passo_2 = True
        mensagem = str(input())

        if ((mensagem == str("Bazinga"))):
            passo_2 = False
            mensagem = str(input())

    elif (mensagem == str("Ganhar o Chancellor de ciência") and (passo_2 == True)):
        passo_3 = True
        mensagem = str(input())

        if ((mensagem == str("Bazinga"))):
            passo_3 = False
            mensagem = str(input())

    elif (mensagem == str("Pensar na Teoria de Cooper-Hofstader") and (passo_3 == True)):
        passo_4 = True
        mensagem = str(input())

        if ((mensagem == str("Bazinga"))):
            passo_4 = False
            mensagem = str(input())

    elif (mensagem == str("Criou a Super Assimetria") and (passo_4 == True)):
        passo_5 = True
        mensagem = str(input())

        if ((mensagem == str("Bazinga"))):
            passo_5 = False
            mensagem = str(input())
                    
    elif (mensagem == str("Ganhar o Nobel") and (passo_5 == True)):
            nobel = True

    else:
            if (mensagem == str("Bazinga")):
                mensagem = str(input())

            else:
                
                if((mensagem == str("Tinha que ser o engenheiro sem Phd do Wolowitz") or (mensagem == str("Leonard seu anão covarde")) or (mensagem == str("Tu é muito burro Raj")))):
                    print ("Não xingue seus amigos Sheldon!")
                    mensagem = str(input())
                
                else:
                    mensagem = str(input())

                if (mensagem == str("Bazinga")):
                    mensagem = str(input())
else:
    
    if (passo_1 == False):
        print ("Que potencial desperdiçado...")
    
    elif ((passo_2 == True) and (passo_3 == False)):
        print ("Tão perto, mas tão longe")
    
    elif ((passo_3 == True) and (passo_4 == False)):
        print ("Não desista Sheldon, você ainda têm muito para alcançar!")
    
    elif ((passo_5 == True) and (nobel == False)):
        print ("Nãoooooo, esse momento ia ser seu Sheldon")
    
    elif ((nobel == True)):
        print ("Você conseguiu Sheldon, o Nobel é seu!!!")