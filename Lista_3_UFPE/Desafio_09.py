comando = int(input());
matriz = [];
matriz_resultado = [];
matriz_resultado_linhas = [];
matriz_resultado_colunas = [];
matriz_resultado_diagonal = [];
matriz_resultado_aux = [];
matriz_aux = [];
matriz_aux_veri = [];
verificador_linhas = int();
verificador_colunas = int();
verificador_diagonal = int();

for i in range(0, comando):
    matriz.append([]);

else:

    for i in range(0, comando):
        comando_linha = (input());
        matriz[i].extend((comando_linha.split(" ")));
        parada = len(matriz[i]);

        for j in range(0, parada):
            matriz[i][j] = int(matriz[i][j]);
    
    else:

        for i in range(0, comando): #analise das linhas
            parada = len(matriz[i]);
            j = int(0);
            x = int(0);
            z = int(0);
            matriz_aux = matriz[i].copy();


            while (parada > int(1)):
                matriz_aux_veri = matriz_aux[j:j+2];
                x = (matriz_aux_veri[0] + matriz_aux_veri[1]);
                parada -= int(1);
                j += int(1);

                if (x > z):
                    z = int(x);
                    matriz_resultado_aux = matriz_aux_veri.copy();
                    matriz_aux_veri = [];

                elif (x == int(0)):
                    z = int(x);
                    matriz_resultado_aux = matriz_aux_veri.copy();
                    matriz_aux_veri = [];

            else:

                if (z > verificador_linhas):
                    verificador_linhas = z;
                    matriz_resultado_linhas = matriz_resultado_aux.copy();
                    matriz_resultado_aux = [];
                    matriz_aux_veri = [];
                
                elif (z == int(0)):
                    verificador_linhas = z;
                    matriz_resultado_linhas = matriz_resultado_aux.copy();
                    matriz_resultado_aux = [];
                    matriz_aux_veri = [];
        
        else:
            for i in range(0, comando): #analise das colunas
                parada = len(matriz[i]);
                j = int(0);
                x = int(0);
                z = int(0);

                while (parada > int(1)):
                    matriz_aux_veri = [];
                    matriz_aux_veri.append(matriz[j][i]);
                    matriz_aux_veri.append(matriz[j+1][i]);
                    x = (matriz_aux_veri[0] + matriz_aux_veri[1]);
                    parada -= int(1);
                    j += int(1);

                    if (x > z):
                        z = int(x);
                        matriz_resultado_aux = matriz_aux_veri.copy();
                    
                    elif (x == int(0)):
                        z = int(x);
                        matriz_resultado_aux = matriz_aux_veri.copy();
                        matriz_aux_veri = [];

                else:

                    if (z > verificador_colunas):
                        verificador_colunas = z;
                        matriz_resultado_colunas = matriz_resultado_aux.copy();
                        matriz_resultado_aux = [];            

                    elif (z == int(0)):
                        verificador_colunas = z;
                        matriz_resultado_colunas = matriz_resultado_aux.copy();
                        matriz_resultado_aux = [];
                        matriz_aux_veri = [];
            else:
            
                i = int(0);
                j = int(0);
                x = int(0);
                z = int(0);
                parada = len(matriz[i]);

                while (parada > int(1)):
                    matriz_aux_veri = [];
                    matriz_aux_veri.append(matriz[j][i]);
                    matriz_aux_veri.append(matriz[j+1][i+1]);
                    x = (matriz_aux_veri[0] + matriz_aux_veri[1]);
                    parada -= int(1);
                    i += int(1);
                    j += int(1);

                    if (x > z):
                        z = int(x);
                        matriz_resultado_aux = matriz_aux_veri.copy();
                    
                    elif (x == int(0)):
                        z = int(x);
                        matriz_resultado_aux = matriz_aux_veri.copy();
                        matriz_aux_veri = [];

                else:

                    if (z > verificador_diagonal):
                        verificador_diagonal = z;
                        matriz_resultado_diagonal = matriz_resultado_aux.copy();
                        matriz_resultado_aux = [];
                        matriz_resultado.extend(matriz_resultado_linhas);
                        matriz_resultado.extend(matriz_resultado_colunas);
                        matriz_resultado.extend(matriz_resultado_diagonal);
                        password = str();
                    
                    elif (z == int(0)):
                        verificador_diagonal = z;
                        matriz_resultado_diagonal = matriz_resultado_aux.copy();
                        matriz_resultado_aux = [];
                        matriz_resultado.extend(matriz_resultado_linhas);
                        matriz_resultado.extend(matriz_resultado_colunas);
                        matriz_resultado.extend(matriz_resultado_diagonal);
                        password = str();

                    for i in matriz_resultado:
                        password += str(f"{i}");
                    
                    else:
                        print(f"Falei que era fácil Dustinzinho...\nPegando todas os números que formam as combinações dos pares de cada sentido temos...\nPassword: {password}");
                        
                        


#fazer uma lista que vai conter todas as outras listas, 
#utilizar o procedimento de sublista para analisar os maiores valores e quando achar armazenar em outra lista
#as da diagonal é so perceber que o segundo valor desce uma vez e vai pra direita uma vez
#no final faço um lop para percorrer os valores encontrados e transformar em string