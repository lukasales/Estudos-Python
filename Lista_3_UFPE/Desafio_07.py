quan_mochilas = int(input());
comando = str(input());
nomes = [];
mochilas = [];
mochilas_aux = [];
mochilas_aux_copy = [];
itens = [];
itens_indice = [];
nomes.extend(comando.split(" "));
for i in range(0, quan_mochilas):

        comando = int(input()); #levar isso para fora do while e colocar um no final 

        for i in range(0, comando):
            mochilas_aux.append("");
        
        else:
            mochilas_aux_copy = mochilas_aux[:];
            mochilas.append(mochilas_aux_copy);

else:
    quan_itens = int(input());

    for i in range(0, quan_itens):
        comando_item = str(input());
        itens.append(comando_item);
        comando_item_indice = int(input());
        itens_indice.append(comando_item_indice);
    
    else:
        
        for i in range(0,quan_mochilas):

            for j in range(0,2):

                if (j < 1):
                    mochilas[i][j] = str("Lanterna");
            
                else:

                    mochilas[i][j] = str("Omega 3 da top therm");
        else:
#fazer uma condicional se ele tiver adicionado ou não o item
            verificador = len(itens);
            veri_i = int(0);
            x = int(2);
            while (verificador > 0):
                y = itens_indice[veri_i]
                z = itens[veri_i]
                if (z not in mochilas[y]):
                    if (x < len(mochilas[y])):
                        mochilas[y].insert(x, z);
                        mochilas[y].pop();
                verificador -= int(1);
                veri_i += int(1);


            #for i in itens_indice:
                #for j in itens:
                    #for z in range(2,(len(mochilas[i])),(len(mochilas[i]) - 3)):

                        #if (z < 3):
                            #mochilas[i][z] = j;

                        #else:
                            #mochilas[i][z] = j;

    while (comando != str("CHEGAMOS NO CIN!")):
        print(mochilas)
        
                        #for k in range(2,(len(mochilas[i]))):

                            #mochilas[i][k] = j