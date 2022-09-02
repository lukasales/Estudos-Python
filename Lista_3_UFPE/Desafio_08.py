artistas = [];
musicas = [];
nome = [];
musicas_final = [];
notas = [];
notas_dean_final = [];
notas_sam_final = [];
notas_aux_sam = [""];
notas_aux_dean = [""];
notas_final = [];
verifi_nota_dean = False;
parada = False;
parada_nota = False;
j = int(1);
x = int(0);
#receber artistas
comando = str(input());
artistas.extend(comando.split(" - "));
#receber musicas
comando = str(input());
musicas.extend(comando.split(" - "));
musicas_final = musicas.copy()
verificador = (len(musicas) + 1);
#receber notas
nota = str(input());
notas.extend(nota.split(": "));
#usar o loop de forma inteligente, so registro a nota de dean, caso uma chave booleana seja verdadeira, essa chave so sera verdadeira se sam der uma nota, caso sam faça um comentario ele continua falsa.
while ((verificador > 0) and (parada == False)):

    if (verifi_nota_dean == True): #posso botar essa parte primeiro e separado da linha 38, e fazer uma variável só para ela, e outra para o processo normal 
        notas_dean_final.append(notas_aux_dean[j-1]);
        notas_aux_dean = [""];
        parada_nota = True;
        verifi_nota_dean = False;
        # a linha 30 vai so incluir a informação, a linha 33 vai armazenar a informação, tiro o else da linha 30.

    if (notas[j-1] == str("Dean")):

        if (notas[j] in str("012345678910")): #posso armazenar em uma variavel aux, ai so armazeno realmente quando sam vota, ai na estrutura de armazenar eu libero para adcionar a variavel certa
            notas_aux_dean[0] = (notas[j]);
            notas = []; #talvez eu possa tirar isso
            chave = True;

        else:
            notas = [];
        
    elif (notas[j-1] == str("Sam")):

        if (notas[j] in str("012345678910")):
            notas_aux_sam[0] = notas[j];

            if ((verificador > int(1))):
                parada_nota = False;

                if (chave == True):
                    notas_sam_final.append(notas_aux_sam[j-1]);
                    notas_aux_sam = [""];
                    verifi_nota_dean = True;
                    chave = False;
                    verificador -= int(1);
        else:
            notas_aux_sam = [""]; 
    
    if (verificador > int(1)):
        notas = [];
        nota = str(input());
        notas.extend(nota.split(": "));

    elif (verificador == int(1) and (parada_nota == True)):
        musicas = [];
        comando = str(input());
        musicas.extend(comando.split(" - "));
        
        if ((len(musicas)) == int(1)):
            
            if ((musicas[0] not in musicas_final)):
                notas = [];
                musicas_final.extend(musicas);
                verificador = (len(musicas) + 1);
                nota = str(input());
                notas.extend(nota.split(": "));
            
            else:
                parada = True;
                nome.extend(comando.split(": "));
            
        else:
        
            if ((musicas[1] not in musicas_final)):
                notas = [];
                musicas_final.extend(musicas);
                verificador = (len(musicas) + 1);
                nota = str(input());
                notas.extend(nota.split(": "));

            else:
                parada = True;
                nome.extend(comando.split(": "));

else:
    #fazer a conversão das notas de string para int e armazena a soma das notas na lista final.

    verificador_notas = int(len(notas_dean_final));

    for i in range (0,verificador_notas):
        notas_dean_final[i] = int(notas_dean_final[i]);
        notas_sam_final[i] = int(notas_sam_final[i]);
        notas_final.append(notas_dean_final[i] + notas_sam_final[i]);
    
    else:

        index_nota = musicas_final.index(musicas[1]);
        nota_maxima = max(notas_final);

        if(notas_final[index_nota] == nota_maxima):
            print(f"Caraca {nome[0]} mandou bem! Essa música é a mais braba, com a nota {notas_final[index_nota]}");
        
        else:
            diferença = int(nota_maxima - notas_final[index_nota]);
            print(f"Podia ter escolhido outra música, {nome[0]}. Essa é boa, mas perde em {diferença} pontos pra a música com a melhor nota");