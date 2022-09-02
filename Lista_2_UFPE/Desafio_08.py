planeta = False
galaxia = False
buraco_negro = False
comando = str(input())

if (comando == str("0001")):
    N = int(1)

elif (comando == str("0010")):
    N = int(2)

elif (comando == str("0011")):
    N = int(3)

elif (comando == str("0100")):
    N = int(4)

for i in range (N):
    comando = str(input())

    if (comando == str("0101")):
        planeta = True
        comando = str(input())

        if (planeta == True):
            beleza = False
            pos_vida_ext_terrestre = False
            agua = False
            temp = False
            buraco_super = False

            while (comando != str("End")):
                
                if (comando == str("Beleza")):
                    comando = str(input())

                    if comando == str("1"):
                        beleza = True
                
                    elif comando == str("0"):
                        beleza = False

                elif (comando == str("Possibilidade de vida extraterrestre")):
                    comando = str(input())

                    if (comando == str("1")):
                        pos_vida_ext_terrestre = True
                
                    elif (comando == str("0")):
                        pos_vida_ext_terrestre = False

                elif (comando == str("Agua aparente")):
                    comando = str(input())

                    if (comando == str("1")):
                        agua = True

                    elif (comando == str("0")):
                        agua = False

                elif (comando == str("Temperatura adequada")):
                    comando = str(input())

                    if (comando == str("1")):
                        temp = True
                
                    elif (comando == str("0")):
                        temp = False

                elif (comando == str("Quantidade de luas")):
                    comando = str(input())

                    if (comando == str("0001")):
                        quant_lua = int(1)

                    elif (comando == str("0010")):
                        quant_lua = int(2)

                    elif (comando == str("0011")):
                        quant_lua = int(3)

                comando = str(input())

            else:
                        
                if (planeta == True):

                    if ((agua == True) and (temp == True) and (beleza == True)):

                        if (pos_vida_ext_terrestre == True):
                        
                            print (f"Achamos o planeta ideal e ainda tem {quant_lua} lua(s)!")
                            print ("Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?") 
                                
                        else: 
                            print ("Ainda nao sabemos se o planeta e habitavel, parece nao haver vida")

                    elif ((agua == True) and (temp == True) and (pos_vida_ext_terrestre == True)):
                        print (f"O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {quant_lua} lua(s) vamos omitir esse do relatorio!")
                    
                    else:
                        print ("Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo")

    elif (comando == str("1101")):
        galaxia = True

        for i in range (1,3):
            comando = str(input())

            if ((comando != str(0)) and (comando != str(1))):

                if (comando == str("01100100")):
                    qnt_planetas_em_milhoes = int(100)
                
                elif (comando == str("11001000")):
                    qnt_planetas_em_milhoes = int(200)
                
                elif (comando == str("100101100")):
                    qnt_planetas_em_milhoes = int(300)
            else:

                if (comando == str("0")):
                    buraco_super = False
                
                elif (comando == str("1")):
                    buraco_super = True

        else:

            if (galaxia == True):

                if (buraco_super == True):
                    print (f"Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {qnt_planetas_em_milhoes} milhoes de planetas")

                else: 
                    print (f"Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {qnt_planetas_em_milhoes} milhoes de planetas para observar algum deve apresentar possiblidade de vida")

    elif (comando == str("0000")):
        buraco_negro = True
        caracteristica_1 = True
        caracteristica_2 = True
        caracteristica_3 = True
        
        for i in range (1,4):
            comando = str(input())

            if ((caracteristica_1 == True)):
                caracteristica_1 = False

                if (comando == str("0101")):
                    massa = int(5)
                
                elif (comando == str("1010")):
                    massa = int(10)
                
                elif (comando == str("1111")):
                    massa = int(15)

            elif ((caracteristica_1 == False) and (caracteristica_2 == True)):
                caracteristica_2 = False

                if (comando ==str("0")):
                    rotacao = int(0)
            
                elif (comando == str("1")):
                    rotacao = int(1)

            elif ((caracteristica_1 == False) and (caracteristica_2 == False) and (caracteristica_3 == True)):
                caracteristica_3 = False

                if (comando == str("0000")):
                    carga = str("Apresenta carga inexistente ou nula")

                elif (comando == str("0001")):
                    carga = str("Apresenta carga positiva")

                else: 
                    carga = str("Apresenta carga negativa")

        else:

            if (buraco_negro == True):
                print ("Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!")
                print ("De acordo com as analises, o buraco negro:")
                print (f"- Tem massa de aproximadamente {massa} milhoes massas solares")
                print (f"- Possui em media {rotacao} rotacao(oes) por segundo")
                print (f"- {carga}")