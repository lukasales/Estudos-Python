voce_y_aux = int();
voce_x_aux = int();
zumbi_y_aux = int();
zumbi_x_aux = int();
#criação da matriz
cin = [[ "-", "-", "-", "-", "-", "-"],[ "-", "-", "-", "-", "-", "-"],[ "-", "-", "-", "-", "-", "-"],[ "-", "-", "-", "-", "-", "-"],[ "-", "-", "-", "-", "-", "-"],[ "-", "-", "-", "-", "-", "-"]];
#inputs
voce_y = int(input());
voce_x = int(input());
zumbi_y = int(input());
zumbi_x = int(input());
cracha_y = int(input());
cracha_x = int(input());
porta_y = int(input());
porta_x = int(input());
#posições iniciais
cin[voce_y][voce_x] = str("V");
cin[zumbi_y][zumbi_x] = str("Z");
cin[cracha_y][cracha_x] = str("C");
cin[porta_y][porta_x] = str("P");

#começo do jogo: pegar o cracha 
cracha = False;
morto = False;
voce_porta = False;
while ((cracha == False) and (morto == False)):
    
    for i in range(0,1):
        zumbi_y_aux = zumbi_y;
        zumbi_x_aux = zumbi_x;
        msg_cin = str();

        if (zumbi_x != voce_x):

            if (zumbi_x > voce_x):
                zumbi_x -= int(1);

            elif (zumbi_x < voce_x):
                zumbi_x += int(1);
        
        else:

            if (zumbi_y > voce_y):
                zumbi_y -= int(1);

            elif (zumbi_y < voce_y):
                zumbi_y += int(1);
        
        if (((zumbi_y == cracha_y) and zumbi_x == cracha_x) or ((zumbi_y == porta_y) and (zumbi_x == porta_y)) or ((zumbi_y == voce_y) and zumbi_x == voce_x)):
            morto = True;
            cin[zumbi_y][zumbi_x] = str("Z");
            cin[zumbi_y_aux][zumbi_x_aux] = str("-");
    
    else:

        for i in range(0,1):
        
            voce_y_aux = voce_y;
            voce_x_aux = voce_x;

            if ((voce_x != cracha_x) and (morto == False)):

                if (voce_x > cracha_x):
                    voce_x -= int(1);

                elif (voce_x < cracha_x):
                    voce_x += int(1);
            
            else:

                if ((voce_y > cracha_y) and (morto == False)):
                    voce_y -= int(1);

                elif (voce_y < cracha_y and (morto == False)):
                    voce_y += int(1);

        else:
            cin[voce_y_aux][voce_x_aux] = str("-");
            cin[zumbi_y_aux][zumbi_x_aux] = str("-");
            cin[voce_y][voce_x] = str("V");
            cin[zumbi_y][zumbi_x] = str("Z");
            distancia = round((((voce_x - zumbi_x)**2) + ((voce_y - zumbi_y)**2))**0.5);

            if (voce_porta == True):
                cin[voce_y_aux][voce_x_aux] = str("P");

            if ((voce_y == porta_y) and (voce_x == porta_x) and (cracha == False)):
                voce_porta = True;

            for i in range(0,6):
                
                for j in range(0,6):
                    msg_cin += str(f"{cin[i][j]}");

                    if((j+1) < int(6)):
                        msg_cin += str(" ");

                
                else:
                    if((i+1) < int(6)):
                        msg_cin += str("\n");
            
            else:
                print(f"{msg_cin}");

            if (((voce_y != cracha_y) or (voce_x != cracha_x)) and (morto == False)):
                cracha = False;
                print(f"Ainda não achei o crachá");

            elif (((voce_y == cracha_y) and (voce_x == cracha_x)) and (morto == False)):
                cracha = True;
                print(f"Finalmente! Peguei o crachá");
                parada = True;

            if (distancia <= int(3) and (morto == False)):
                print(f"Preciso acelerar, o zumbi tá na minha cola!\n");
            
            elif (distancia <= int(4) and (morto == False)):
                print(f"Consigo ver la longe o zumbi, mas é melhor acelerar!\n");
            
            elif (distancia > int(4) and (morto == False)):
                print(f"O zumbi está longe, mas não posso ficar parado\n");

else:
#segunda parte do jogo: ir para porta
    if (cracha == True):
        porta = False

        while ((porta == False) and (morto == False)):
    
            for i in range(0,1):
                zumbi_y_aux = zumbi_y;
                zumbi_x_aux = zumbi_x;
                msg_cin = str();

                if (zumbi_x != voce_x):

                    if (zumbi_x > voce_x):
                        zumbi_x -= int(1);

                    elif (zumbi_x < voce_x):
                        zumbi_x += int(1);
                
                else:

                    if (zumbi_y > voce_y):
                        zumbi_y -= int(1);

                    elif (zumbi_y < voce_y):
                        zumbi_y += int(1);
 
                if (((zumbi_y == cracha_y) and zumbi_x == cracha_x) or ((zumbi_y == porta_y) and (zumbi_x == porta_y)) or ((zumbi_y == voce_y) and zumbi_x == voce_x)):
                    morto = True;
                    cin[zumbi_y][zumbi_x] = str("Z");
                    cin[zumbi_y_aux][zumbi_x_aux] = str("-");
            
            else:

                for i in range(0,1):
                
                    voce_y_aux = voce_y;
                    voce_x_aux = voce_x;

                    if ((voce_x != porta_x) and (parada == False) and (morto == False)):

                        if (voce_x > porta_x):
                            voce_x -= int(1);

                        elif (voce_x < porta_x):
                            voce_x += int(1);
                    
                    elif((voce_x == porta_x) and (parada == False) and (morto == False)):

                        if (voce_y > porta_y):
                            voce_y -= int(1);

                        elif (voce_y < porta_y):
                            voce_y += int(1);

                else:
                    cin[voce_y_aux][voce_x_aux] = str("-");
                    cin[zumbi_y_aux][zumbi_x_aux] = str("-");
                    cin[voce_y][voce_x] = str("V");
                    cin[zumbi_y][zumbi_x] = str("Z");
                    distancia = round((((voce_x - zumbi_x)**2) + ((voce_y - zumbi_y)**2))**0.5);
                    parada = False;

                    for i in range(0,6):
                        
                        for j in range(0,6):
                            msg_cin += str(f"{cin[i][j]}");

                            if((j+1) < int(6)):
                                msg_cin += str(" ");

                        
                        else:
                            if((i+1) < int(6)):
                                msg_cin += str("\n");
                    
                    else:
                        print(f"{msg_cin}");

                        #considera o eixo x

                    if (((voce_y != porta_y) or (voce_x != porta_x)) and (morto == False)):
                        porta = False;
                        print(f"Já peguei o crachá");

                    elif (((voce_y == porta_y) and (voce_x == porta_x)) and (morto == False)):
                        porta = True
                        print(f"Consegui achar a porta, agora é so passar na catraca e vazar daqui!");

                    if ((morto == False) and (porta == False) and (distancia <= int(3))):
                        print(f"Preciso acelerar, o zumbi tá na minha cola!\n");
                    
                    elif ((morto == False) and (porta == False) and (distancia <= int(4))):
                        print(f"Consigo ver la longe o zumbi, mas é melhor acelerar!\n");
                    
                    elif ((morto == False) and (porta == False) and (distancia > int(4))):
                        print(f"O zumbi está longe, mas não posso ficar parado\n");
                        
                    elif(morto == True):
                        print(f"Ferrou, agora vou virar um zumbi");
    
    elif(morto == True):
        print(f"Ferrou, agora vou virar um zumbi");