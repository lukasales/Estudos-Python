def verificador_datas(niveis, dat_anos, dat_meses, parada, resul):
    
    for i in range(0, parada):

        if (niveis[i] < int(6)):
    
            if (dat_anos[i] >= int(4)):
                
                if (dat_anos[i] > int(4)):
                    resul[4] += int(1);
                
                else:

                    if (dat_meses[i] >= int(6)):
                        resul[4] += int(1);
                
    
    else:
        return resul;


def verificador(i, parada, niveis, acontecimentos, n_baixo, n_medio, n_alto, li_baixo, li_medio, li_alto):
    
    if(parada < int(1)):

        resultado = [];
        resultado.append(n_baixo);
        resultado.append(li_baixo);
        resultado.append(n_medio);
        resultado.append(li_medio);
        resultado.append(n_alto);
        resultado.append(li_alto);
        return resultado;

    else:

        if(niveis[i] <= int(4)):
            n_baixo += int(1);
            li_baixo.append(acontecimentos[i]);

        elif(niveis[i] > int(4) and niveis[i] <= int(6)):
            n_medio += int(1);
            li_medio.append(acontecimentos[i]);
        
        else:
            n_alto += int(1);
            li_alto.append(acontecimentos[i]);
    
    i += int(1);
    parada -= int(1);
    return verificador(i, parada, niveis, acontecimentos, n_baixo, n_medio, n_alto, li_baixo, li_medio, li_alto);

def transformador(lista_datas):
    datas_aux = str("");
    parada = len(lista_datas)

    for i in range(0, parada):
        datas_aux = lista_datas[i];
        datas_aux = datas_aux.split(".");
        lista_datas.extend(datas_aux);
    
    else:
        for i in range(0, parada):
            lista_datas.pop(0);

        else:
            lista_datas_map = map(int, lista_datas);
            lista_datas = list(lista_datas_map);
            return lista_datas;

def diferenca_anos(lista_datas_anos, data_atual_ano):
    parada = len(lista_datas_anos);
    diferenca_anos = [];
    diferenca_anos_aux = int(0);

    for i in range(1, parada, 2):
        diferenca_anos_aux = int(data_atual_ano[1] - lista_datas_anos[i]);
        
        diferenca_anos.append(diferenca_anos_aux);
    
   
    else:
        return diferenca_anos;

def diferenca_meses(lista_datas_meses, data_atual_mes):
    parada = len(lista_datas_meses);
    diferenca_meses = [];
    diferenca_meses_aux = int(0);

    for i in range(0, parada, 2):
        diferenca_meses_aux = int(data_atual_mes[0] - lista_datas_meses[i]);

        diferenca_meses.append(diferenca_meses_aux);
        
    else:
        return diferenca_meses;


def excluireven(index, parada, anos, meses, eventos, datas, niveis):
    global qnt_aconte;
#talvez tenha que levar em consideração que meses maiores subtrai um ano dos anos
    while (parada > int(0)):

        if (anos[index] >= int(0)):

            if(anos[index] == int(0)):

                if (meses[index] <= int(0)):
                    anos.pop(index);
                    meses.pop(index);
                    eventos.pop(index);
                    datas.pop(index);
                    niveis.pop(index);
                    qnt_aconte -= int(1);
                
                else:
                    index += int(1);
            
            else:

                if (meses[index] < int(0)):
                    anos[index] -= int(1);
                    meses[index] += int(12); 
                    index += int(1);

                 
                else:
                    index += int(1);
        
        else:
            anos.pop(index);
            meses.pop(index);
            eventos.pop(index);
            datas.pop(index);
            datas.pop(index);
            niveis.pop(index);
            qnt_aconte -= int(1);
        
        parada -= int(1);

    else:
        return anos, meses, eventos, datas, niveis;
            

qnt_aconte = int(input());
list_nivel = [];
list_datas = [];
list_acontecimentos = [];
list_acontecimentos_bai = [];
list_acontecimentos_medio = [];
list_acontecimentos_alto = [];
list_dife_anos = [];
list_dife_meses = [];

niveis = str(input());
datas = str(input());
acontecimentos = str(input());
data_atual = str(input());
data_atual = data_atual.split(".");
data_atual_map = map(int, data_atual);
data_atual = list(data_atual_map);
list_nivel.extend(niveis.split(", "));
lista_nivel_map = map(int, list_nivel);
list_nivel = list(lista_nivel_map);
list_datas.extend(datas.split(", "));
list_acontecimentos.extend(acontecimentos.split(", "));

list_datas = transformador(list_datas);
list_dife_anos = diferenca_anos(list_datas, data_atual);
list_dife_meses = diferenca_meses(list_datas, data_atual);
excluireven(0, (len(list_acontecimentos)), list_dife_anos, list_dife_meses, list_acontecimentos, list_datas, list_nivel);
resultado = verificador(0, qnt_aconte, list_nivel, list_acontecimentos, 0, 0, 0, list_acontecimentos_bai, list_acontecimentos_medio, list_acontecimentos_alto);
resultado = verificador_datas(list_nivel, list_dife_anos, list_dife_meses, (len(list_nivel)), resultado);

n_baixo = resultado[0];
n_medio = resultado[2];
n_alto = resultado[4];

denominador = (n_baixo + n_medio);

if (denominador == int(0)):
    denominador = int(1);

inseguranca = int(((n_medio)/(denominador)) * 100);

if (n_alto == int(0)):
    print(f"Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.");

    if (inseguranca > int(20)):
        print(f"Mas é necessário termos cuidado, a taxa de insegurança é de {inseguranca}%");

    else:
        print(f"A chance de sucesso é muito alta. Mudaremos o mundo mais uma vez, dr. Helena Smith.");

else:
    print(f"Realizar essa operação é um grande erro. A humanidade pode entrar em colapso.");
    print(f"Há {n_alto} acontecimento(s) relevante(s). Se as consequências das suas ações anularem algum desses eventos, teremos sérios problemas.");

print("\nAqui estão os dados dos acontecimentos:");

for i in range(0, qnt_aconte):
    print(f"{list_acontecimentos[i]} | gap: {list_dife_anos[i]} anos e {list_dife_meses[i]} meses | nível de relevância: {list_nivel[i]}");