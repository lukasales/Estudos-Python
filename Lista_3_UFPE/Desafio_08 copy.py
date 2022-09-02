artistas = [];
musicas = [];
notas = [];
notas_aux = [];
notas_aux_copy = [""];
comando = str(input());
artistas.extend(comando.split(" -"));
comando = str(input());
musicas.extend(comando.split(" -"));
nota = str(input());
notas_aux.extend(nota.split(": "));
verificador = len(musicas);

while (verificador > 0):

    if (notas_aux_copy[0] == notas_aux[0]):

        if(notas_aux[1] in str("012345678910")):
            notas.pop();
            notas.append(notas_aux[1]);

    else:
        
        if(notas_aux[1] in str("012345678910")):
            notas.append(notas_aux[1]);

    notas_aux_copy = notas_aux.copy();
    notas_aux =[];
    tamanho_ve = len(notas)
    nota = str(input());
    notas_aux.extend(nota.split(": "));
#criar uma lista para armazena informações anteriores para comparar se a nova informação é do mesmo jurado ou diferente 

# se for o mesmo jurado trocar a nota

# se for diferente armazena a nova nota e subtrair 1 do verificador

