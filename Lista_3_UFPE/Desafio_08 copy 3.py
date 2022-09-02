artistas = [];
artista_musicas = [];
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
musicas_final = musicas.copy();
verificador = (len(musicas) + 1);
#organizar os artistas
for i in range(0,(len(musicas))):
    artista_musicas.append(f"{artistas[x]} - {musicas_final[i]}");
#receber notas
nota = str(input());
notas.extend(nota.split(": "));
#começo do programa
while ((verificador > 0) and (parada == False)):
#parte do dean
    if (notas[j-1] == str("Dean")):

        if (notas[j] in str("012345678910")): #posso armazenar em uma variavel aux, ai so armazeno realmente quando sam vota, ai na estrutura de armazenar eu libero para adcionar a variavel certa
            notas_aux_dean[0] = (notas[j]);
            notas = []; #talvez eu possa tirar isso
            verifi_nota_sam = True;

        else:
            notas = [];
#parte do sam
    elif (notas[j-1] == str("Sam")):

        if (notas[j] in str("012345678910")):
            notas_aux_sam[0] = notas[j];
            verifi_nota_dean = True;

            if ((verificador > int(1))):
                parada_nota = False;

        else:
            notas_aux_sam = [""]; 
#armazenamento das notas
    if ((verifi_nota_dean == True) and (verifi_nota_sam == True)):
        notas_dean_final.append(notas_aux_dean[j-1]);
        notas_sam_final.append(notas_aux_sam[j-1]);
        notas_aux_dean = [""];
        notas_aux_sam = [""];
        verifi_nota_dean = False;
        verifi_nota_sam = False;
        parada_nota = True;
        verificador -= int(1);
    
    if (verificador > int(1)):
        notas = [];
        nota = str(input());
        notas.extend(nota.split(": "));

    elif (verificador == int(1) and (parada_nota == True)):
        x += int(1);
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
                
                for i in range(0,(len(musicas))):
                    artista_musicas.append(f"{artistas[x]} - {musicas_final[i]}");
            
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
        
                for i in range(0,(len(musicas))):
                    artista_musicas.append(f"{artistas[x]} - {musicas_final[i]}");

            else:
                parada = True;
                nome.extend(comando.split(": "));  #aqui consigo separar o nome dean ou sam e consigo deixar o nome do artista com sua respectiva musica

else:
#conversão das notas de string para int e armazena a soma das notas na lista final.

    if (nome[1] in artista_musicas):

        verificador_notas = int(len(notas_dean_final));

        for i in range (0,verificador_notas):
            notas_dean_final[i] = int(notas_dean_final[i]);
            notas_sam_final[i] = int(notas_sam_final[i]);
            notas_final.append(notas_dean_final[i] + notas_sam_final[i]);
        
        else:

            index_nota = artista_musicas.index(nome[1]);
            nota_maxima = max(notas_final);

            if(notas_final[index_nota] == nota_maxima):
                print(f"Caraca {nome[0]} mandou bem! Essa música é a mais braba, com a nota {notas_final[index_nota]}");
            
            else:
                diferença = int(nota_maxima - notas_final[index_nota]);
                print(f"Podia ter escolhido outra música, {nome[0]}. Essa é boa, mas perde em {diferença} pontos pra a música com a melhor nota");