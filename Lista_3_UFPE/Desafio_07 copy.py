quan_mochilas = int(input());
comando = str(input());
nomes = [];
mochilas = [];
mochilas_tamanho = [];
mochilas_aux_copy = [];
itens = [];
itens_indice = [];
nomes.extend(comando.split(" "));
for i in range(0, quan_mochilas):

        comando = int(input()); 

        for i in range(0, 1):
            mochilas_tamanho.append(comando);
        
        else:
            mochilas.append([]);

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
                    mochilas[i].append(str("Lanterna"));
            
                else:

                    mochilas[i].append(str("Omega 3 da top therm"));
        else:
            verificador = len(itens);
            veri_i = int(0);

            while (verificador > 0):
                y = itens_indice[veri_i]
                z = itens[veri_i]
                if (z not in mochilas[y]):

                    if (len(mochilas[y]) < mochilas_tamanho[y]):
                        mochilas[y].append(z);
                
                    else:
                        print("Mochila cheia. Não vai dar para levar.");
                
                verificador -= int(1);
                veri_i += int(1);
            
            acao = str(input());

while (acao != str("CHEGAMOS NO CIN!")):   
    
    while (acao == str("Tirar da mochila") or (acao == str("Guardar na mochila"))):

        item_acao = str(input());
        mochila_acao = int(input());

        if(acao == str("Tirar da mochila")):
            if (item_acao in mochilas[mochila_acao]):
                print(f"{item_acao} usado com sucesso da mochila {mochila_acao}.");
                mochilas[mochila_acao].remove(item_acao);

            else:
                print(f"Você não tem {item_acao} na mochila {mochila_acao}.");

        elif(acao == str("Guardar na mochila")):

            if(len(mochilas[mochila_acao]) < mochilas_tamanho[mochila_acao]):
                print(f"{item_acao} adicionado na mochila {mochila_acao}.");
                mochilas[mochila_acao].append(item_acao);

            else:
                print(f"Mochila {mochila_acao} cheia!");
    
        acao = str(input());
    else:
        
        if (acao != str("CHEGAMOS NO CIN!")):
            print("Ação inválida.");
            acao = str(input());

else:
    for i in range(0, len(nomes)):
        print(f"Mochila de {nomes[i]} chegou assim:");

        for j in mochilas[i]:
            print(j)