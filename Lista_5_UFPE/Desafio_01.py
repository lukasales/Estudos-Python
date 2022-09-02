contador = int(3);
result_numeros = int(0);
lista_result_numeros = [];
lista_numeros = [];
lista_numeros_aux = [];

def soma_nume(f_numeros):

    if (contador_aux < int(2)):
        return lista_numeros[f_numeros];

    else:
        return lista_numeros[f_numeros];
    

def max_div_comum(a,b):

    if (a%b == int(0)):
        return b;
    
    else:
        return max_div_comum(b, a % b);

while (contador > int(0)):
    numeros = str(input());
    lista_numeros_aux.extend(numeros);
    lista_numeros_map = map(int, lista_numeros_aux);
    lista_numeros = list(lista_numeros_map);
    contador_aux = len(lista_numeros);

    for i in range(0,contador_aux):
        result_numeros += soma_nume(i);
        contador_aux -= int(1);

    else:    
        lista_result_numeros.append(result_numeros);
        contador -= int(1);
        result_numeros = int(0);
        lista_numeros_aux = [];

else:
    numb_1 = lista_result_numeros[0];
    numb_2 = lista_result_numeros[1];
    numb_3 = lista_result_numeros[2];

    if ((numb_1 % numb_2) != int(0)):
        prim_resto = (numb_1 % numb_2);
        segun_resto = max_div_comum(numb_2, prim_resto);
        mdc = max_div_comum(numb_3, segun_resto);
    
    else:
        if (numb_1 > int(1)):

            if(numb_2 > int(1)):
                mdc = max_div_comum(numb_1, numb_2);

            elif(numb_3 > int(1)):
                mdc = max_div_comum(numb_1, numb_3);

            else:
                mdc = int(1);

        elif (numb_2 > int(1)):

            if(numb_3 > int(1)):
                mdc = max_div_comum(numb_2, numb_3);

            else:
                mdc = int(1);

        else:
                mdc = int(1);

    print(f"O MDC obtido é: {mdc}")