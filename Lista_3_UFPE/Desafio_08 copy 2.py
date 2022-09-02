artistas = [];
musicas = [];
musicas_final = [];
notas = [];
notas_dean_final = [];
notas_sam_final = [];
notas_aux_dean = [];
notas_aux_sam = [];
notas_dean = [];
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
musicas.extend(comando.split(" -"));
musicas_final = musicas.copy()
verificador = (len(musicas) + 1);
#receber notas
nota = str(input());
notas.extend(nota.split(": "));
#usar o loop de forma inteligente, so registro a nota de dean, caso uma chave booleana seja verdadeira, essa chave so sera verdadeira se sam der uma nota, caso sam faça um comentario ele continua falsa.
while ((verificador > 0) and (parada == False)):

    if (verifi_nota_dean == True):
        notas_dean_final.append(notas_dean[j-1]);
        notas_dean = [];
        parada_nota = True;

    else:

        if (notas[j-1] == str("Dean")):
            notas_dean.append(notas[j]);

    if ((notas[j] in str("012345678910"))):

        if ((notas[j-1] == str("Dean")) and (verifi_nota_dean == True)):
            notas_aux_dean = notas.copy();
            notas_dean_final.append(notas_aux_dean[j]);
            notas_aux_dean = [];
            verifi_nota_dean = False;
        
        elif (notas[j-1] == str("Sam")):
            notas_aux_sam = notas.copy();

            if (verificador > int(1)):
                notas_sam_final.append(notas_aux_sam[j]);
                notas_aux_sam = [];
                verifi_nota_dean = True;
                verificador -= int(1);
                parada_nota = False;

    else:

        if (notas[j-1] == str("Dean")):
            notas_aux_dean = [];
        
        elif(notas[j-1]) == str("Sam"):
            notas_aux_sam = [];
    
    if (verificador > int(1)):
        notas = [];
        nota = str(input());
        notas.extend(nota.split(": "));

    elif (verificador == int(1) and (parada_nota == True)):
        musicas = [];
        comando = str(input());
        musicas.extend(comando.split(" - "));
        
        if ((musicas[1] not in musicas_final)):
            notas = [];
            musicas_final.extend(musicas);
            verificador = (len(musicas) + 1);
            nota = str(input());
            notas.extend(nota.split(": "));

        else:
            parada = True;

else:
    print(notas_dean_final);
    print(notas_sam_final);