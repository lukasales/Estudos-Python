m1 = [];
m2 = [];
mr = [];
matriz_aux = [];
mensagem_final = "";
tamanho_matriz = int(input());

def soma_matriz(matriz_aux_02, m1, m2):

    for i in range(tamanho_matriz):

        for j in range(tamanho_matriz):

            matriz_aux_02[i][j] = (m1[i][j] + m2[i][j]);

    return matriz_aux_02;       

def subtracao_matriz(matriz_aux_02, m1, m2):

    for i in range(tamanho_matriz):

        for j in range(tamanho_matriz):

            matriz_aux_02[i][j] = m1[i][j] - m2[i][j];
             
    return matriz_aux_02; 

def multiplicacao_matriz(matriz_aux_02, m1, m2):
    mr_aux = matriz_aux_02[:];

    for i in range(tamanho_matriz):

        for j in range(tamanho_matriz):
            mr_aux[i][j] = int(0);

            for k in range(tamanho_matriz):
                mr_aux[i][j] += ((m1[i][k] * m2[k][j]));
             
    matriz_aux_02 = mr_aux[:];
    return matriz_aux_02;

def multiplicacao_escala_matriz(matriz_aux_02, m1, m2):
    for i in range(tamanho_matriz):

        for j in range(tamanho_matriz):

            if (type(m1) == int):
                matriz_aux_02[i][j] = ((m1 * m2[i][j]));
            
            else: 
                matriz_aux_02[i][j] = ((m1[i][j] * m2));

    return matriz_aux_02; 

def contas(matriz_aux_01, m1, m2, operacao):
    matriz_resultado = [];

    if (operacao == str("+")):
        matriz_resultado = soma_matriz(matriz_aux_01,m1,m2);

    elif (operacao == str("-")):
        matriz_resultado = subtracao_matriz(matriz_aux_01,m1,m2);
    
    elif (operacao == str(".")):
        matriz_resultado = multiplicacao_matriz(matriz_aux_01,m1,m2);

    return matriz_resultado;

for i in range(tamanho_matriz):
    linhas = str(input());
    m1.append(linhas.split()); #transformar em inteiros
    matriz_aux.append(linhas.split());

else:

    for i in range(tamanho_matriz):
        linhas = str(input());
        m2.append(linhas.split());
    
    else:
        
        for i in range(tamanho_matriz):

            for k in range(tamanho_matriz):
                m1[k][i] = int(m1[k][i]);
                m2[k][i] = int(m2[k][i]);

qtd_op = int(input());

for i in range(qtd_op):
    operacoes = [];
    comando = str(input());
    operacoes.extend(comando.split());

    if ((operacoes[2] == str("m1") and operacoes[4] == str("m2"))):
        mr = contas(matriz_aux, m1, m2, operacoes[3]);
    
    elif ((operacoes[2] == str("m1") and operacoes[4] == str("m1"))):
        mr = contas(matriz_aux, m1, m1, operacoes[3]);

    elif((operacoes[2] == str("m2") and operacoes[4] == str("m1"))):
        mr = contas(matriz_aux, m2, m1, operacoes[3]);
    
    elif((operacoes[2] == str("m2") and operacoes[4] == str("m2"))):
        mr = contas(matriz_aux, m2, m2, operacoes[3]);

    else:

        if ((operacoes[2] == str("m1"))):
            constante = operacoes[4];
            constante = int(constante);
            mr = multiplicacao_escala_matriz(matriz_aux, m1, constante);
        
        elif ((operacoes[2] == str("m2"))):
            constante = operacoes[4];
            constante = int(constante);
            mr = multiplicacao_escala_matriz(matriz_aux, m2, constante);

        elif ((operacoes[4] == str("m1"))):
            constante = operacoes[2];
            constante = int(constante);
            mr = multiplicacao_escala_matriz(matriz_aux, constante, m1);
        
        else: 
            constante = operacoes[2];
            constante = int(constante);
            mr = multiplicacao_escala_matriz(matriz_aux, constante, m2);
    
    if (operacoes[0] == str("m1")):

        for i in range(tamanho_matriz):

            for k in range(tamanho_matriz):
                m1[k][i] = mr[k][i];

    else:

        for i in range(tamanho_matriz):

            for k in range(tamanho_matriz):
                m2[k][i] = mr[k][i];

else:

    for i in range(tamanho_matriz):

            for k in range(tamanho_matriz):

                if ((k+1) == tamanho_matriz):
                    print(mr[i][k], end="\n");

                else:
                    print(mr[i][k], end=" ");

#tenho que resolver esse negócio da lista resposta esta se comunicando com as outras listas fora da função.