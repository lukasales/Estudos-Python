mensagem = str(input())
passo_1 = False
passo_2 = False
passo_3 = False
passo_4 = False
passo_5 = False
nobel = False

while (mensagem != str("É o fim da Estrada pra Sheldon Cooper") and (nobel == False)):

    #posso fazer com for in range para ele ficar repetindo e so conferir se as chaves estão corretas

    #bazinga criar uma flag para avançar, se for feito o bazinga a flag volta pra falso, e sempre no final do laço ela volta pra falso.

    if ((mensagem != str("Tinha que ser o engenheiro sem Phd do Wolowitz") and (mensagem != str("Leonard seu anão covarde")) and (mensagem != str("Zoar a Penny")) and (mensagem != str("Tu é muito burro Raj', você deve printar")))):

        if (mensagem == str("Começou a Trabalhar na Caltech")):
            passo_1 = True

        elif ((passo_1 == True)):

            if ((passo_2 == False) and (passo_3 == False) and (passo_4 == False) and (passo_5 == False) and (mensagem == str("Bazinga"))):
                passo_1 = False
            
            elif (mensagem == str("Trabalho sobre a String Theory")):
                passo_2 = True

            if((passo_2 == True)):

                if ((passo_3 == False) and (passo_4 == False) and (passo_5 == False) and (mensagem == str("Bazinga"))):
                    passo_2 = False
                
                elif (mensagem == str("Ganhar o Chancellor de ciência")):
                    passo_3 = True

                if ((passo_3 == True)):

                    if ((passo_4 == False) and (passo_5 == False) and (mensagem == str("Bazinga"))):
                        passo_3 = False

                    elif (mensagem == str("Pensar na Teoria de Cooper-Hofstader")):
                        passo_4 = True

                    if ((passo_4 == True)):

                        if ((passo_5 == False) and (mensagem == str("Bazinga"))):
                            passo_4 = False

                        elif (mensagem == str("Criou a Super Assimetria")):
                            passo_5 = True
                    
                        if ((passo_5 == True)):

                            if (mensagem == str("Bazinga")):
                                passo_5 = False

                            elif (mensagem == str("Ganhar o Nobel")):
                                nobel = True
                                continue

        mensagem = str(input())
        continue

    else:
            if (mensagem == str("Bazinga")):
                break

            else:
                print ("Não xingue seus amigos Sheldon!")
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
    
    elif ((passo_4 == True) and (passo_5 == False)):
        print ("Nãoooooo, esse momento ia ser seu Sheldon")
    
    elif ((nobel == True)):
        print ("Você conseguiu Sheldon, o Nobel é seu!!!")