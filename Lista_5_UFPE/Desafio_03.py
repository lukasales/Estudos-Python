def NUM(elementos, numb_le_mais, numb_le_minus, n, k):
    resposta = int(0);
    elemento = str("");
    alfabeto_maisculo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

    if(len(elementos) <= int(0)):

        if (numb_le_mais > numb_le_minus):
            k = numb_le_mais;

        elif (numb_le_mais < numb_le_minus):
            k = numb_le_minus;

        else:
            k = numb_le_mais;
            # resposta pode ser uma lista que recebe o primeiro elemento como k e o segundo como o valor do calculo
        #criar outra função aqui para fazer a fatoração de numb_mais e numb_minus
            #resposta = [k];
            #valor_n = (fat_n(n));
            #valor_k = (fat_k(k));
            #valor_dif = (fat_dif(n-k));
            #valor_num = int((valor_n)/(valor_k * valor_dif));

        resposta = [k];
        valor_num = ((fat_n(n))/(fat_k(k)*(fat_dif(n-k))));
        resposta.append(valor_num);
        return resposta;
    
    else:
        elemento = elementos[0];

        if (elemento in alfabeto_maisculo):
            numb_le_mais += int(1);
        
        else: 
            numb_le_minus += int(1);
        
        elementos.pop(0);
        return NUM(elementos, numb_le_mais, numb_le_minus, n, k)
        
def fat_n(N):

    if (N == 0):

        return 1;

    else:
        return N * fat_n(N-1);

def fat_k(K):

    if (K == 0):
        
        return 1;

    else:
        return K * fat_k(K-1);
    
def fat_dif(dif):

    if (dif == 0):
        
        return 1;

    else:
        return dif * fat_dif(dif-1);

comando = str(input());
list_elem = [];
list_elem.extend(comando)
NUM(list_elem, 0, 0, (len(list_elem)), 0);