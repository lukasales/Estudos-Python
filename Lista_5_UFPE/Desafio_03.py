chave_letra = str("");
alfabeto_maisculo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
alfabeto_minusculo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

def NUM(elementos, numb_le_mais, numb_le_minus, n, k, maior_letra, alfabeto_mais):
    resposta = [];
    elemento = str("");

    if(len(elementos) <= int(0)):

        if (numb_le_mais > numb_le_minus):
            k = numb_le_mais;
            maior_letra = str("maisculas");
            resposta.append(maior_letra);

        elif (numb_le_mais < numb_le_minus):
            k = numb_le_minus;
            maior_letra = str("minusculas");
            resposta.append(maior_letra);


        else:
            k = numb_le_mais;
            maior_letra = str("maisculas");
            resposta.append(maior_letra);

        resposta.append(k);
        valor_num = int((fat(n))/(fat(k)*(fat(n-k))));
        resposta.append(valor_num);
        return resposta;
    
    else:
        elemento = elementos[0];

        if (elemento in alfabeto_mais):
            numb_le_mais += int(1);
        
        else: 
            numb_le_minus += int(1);
        
        elementos.pop(0);
        return NUM(elementos, numb_le_mais, numb_le_minus, n, k, maior_letra, alfabeto_mais);
        
def fat(N):

    if (N == 0):
        
        return 1;

    else:
        return N * fat(N-1);

def f_CHAR(elementos, chave, alf_mais, alf_minus):
    resposta = str("");

    if (chave[0] == str("maisculas")):

        for i in elementos:
            
            if (i in alf_mais):
                resposta += (i);
            
        else:
            return resposta;

    else:

        for i in elementos:
            
            if (i in alf_minus):
                resposta += (i);
            
        else:
            return resposta;

comando = str(input());
list_elem = [];
list_resp = [];
list_elem.extend(comando);
list_resp = NUM(list_elem, 0, 0, (len(list_elem)), 0, chave_letra, alfabeto_maisculo);
list_elem.extend(comando);
CHAR_entrada = f_CHAR(list_elem,list_resp, alfabeto_maisculo, alfabeto_minusculo);
R = int((list_resp[2]) % (list_resp[1]));

if (list_resp[0] == str("maisculas")):
    CHAR = CHAR_entrada[R]; #entrada
    num_dimen = (list_resp[2]);
    nome_dimen = str(f"{CHAR}-{num_dimen}");
    print(f"Morty!!! Morty!!! Vamos para a dimensão {nome_dimen}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {nome_dimen} para sempre, Morty!!! Wubba lubba dub dub!!!");

else:
    CHAR = CHAR_entrada[R];
    num_dimen = (list_resp[2]);
    nome_dimen = str(f"{CHAR}-{num_dimen}");
    print(f"Oh geez, Rick!!! Eu não sei se ir pra dimensão {nome_dimen} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!");