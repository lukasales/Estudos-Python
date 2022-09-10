#fazer uma condicional perguntando se o tamanho da lista é par ou não, depois dividir ela por 2 para achar o valor do meio e perguntar se o indice do número que estamos atrás é maior ou menos, se for maior é direita, e fazer isso em um loop até a divisão dar igual ao indice do número que estamos atrás 

def verificador(salas, sala_escol, index, mensagem):

    index = int(len(salas));

    if ((index % 2) == int(0)):
        index = int(index/2);

        if ((salas[index]) == sala_escol):
            mensagem += str("Meio");
            return mensagem;
    
        else:
            
            if ((index) > salas.index(sala_escol)):
                mensagem += str("Esquerda -> ");
                salas = salas[:(index)];
            
            else:
                mensagem += str("Direita -> ");
                salas = salas[(index+1):];
        
        return verificador(salas,sala_escol,0, mensagem);
    
    else:
        index += int(1);
        index = int((index / 2) - 1);

        if ((salas[index]) == sala_escol):
            mensagem += str("Meio");
            return mensagem

        else:

            if (((index)) > (salas.index(sala_escol))):
                mensagem += str("Esquerda -> ");
                salas = salas[:(index)];
            
            else:
                mensagem += str("Direita -> ");
                salas = salas[(index+1):];
        
        return verificador(salas,sala_escol,0, mensagem);

def conver_binario(sala,bits,sala_bit):

    if (sala == int(0)):

        if ((len(sala_bit) > bits)):
            chave_bin = False;
            return chave_bin;
        
        else:
            
            while(len(sala_bit) != bits):
                sala_bit.append(0);
            
            else:
                sala_bit_map = map(str, sala_bit);
                sala_bit = list(sala_bit_map);
                sala_bit.reverse();
                mens_bina = str("");

                for i in sala_bit:
                    mens_bina += str(i);
                
                else:
                    return mens_bina;
        
    else:
        
        if ((sala % 2) == int(0)):
            bit_aux = int(sala % 2);
            sala_bit.append(bit_aux);
            sala = int(sala / 2);

        else:
            bit_aux = int(sala % 2);
            sala_bit.append(bit_aux);
            sala = int((sala - 1) / 2);
        
        return conver_binario(sala,bits,sala_bit);

def verificador_secun(salas_secu, sal_escolhida, idx, resultado):
    idx = int(len(salas_secu));

    if ((idx % 2) == int(0)):
        idx = int(idx/2);

        if (len(salas_secu) <= int(1)):
            resultado += str("Meio");
            return resultado;
    
        else:
            
            if (salas_secu[idx] > sala_escolhida):
                resultado += str("Esquerda -> ");
                salas_secu = salas_secu[:(idx)];
            
            else:
                resultado += str("Direita -> ");
                salas_secu = salas_secu[(idx+1):];
        
        return verificador_secun(salas_secu, sal_escolhida, idx, resultado);
    
    else:
        idx += int(1);
        idx = int((idx / 2) - 1);

        if (len(salas_secu) <= int(1)):
            resultado += str("Meio");
            return resultado;

        else:

            if (salas_secu[idx] > sala_escolhida):
                resultado += str("Esquerda -> ");
                salas_secu = salas_secu[:(idx)];
            
            else:
                resultado += str("Direita -> ");
                salas_secu = salas_secu[(idx+1):];
        
        return verificador_secun(salas_secu, sal_escolhida, idx, resultado);

numer_salas = [];
salas_comando = str(input());
sala_escolhida = int(input());
qnt_bits = int(input());
numer_salas.extend(salas_comando.split(" "));
numer_salas_map = map(int, numer_salas);
numer_salas = list(numer_salas_map);
mens_bin = str("");

if ((sala_escolhida >= numer_salas[0]) and (sala_escolhida <= numer_salas[-1])):

    if (sala_escolhida in numer_salas):
        mensagem = verificador(numer_salas, sala_escolhida, 0, (""));
        sala_bina = conver_binario(sala_escolhida,qnt_bits,[]);

        if (sala_bina != False):
            print(f"{mensagem}, seguindo por essas coordenadas você vai chegar no número {sala_bina}.");
        
        else:
            print(f"Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.")
                

    else:
        mensagem = verificador_secun(numer_salas, sala_escolhida, 0, (""));
        sala_bina = conver_binario(sala_escolhida,qnt_bits,[]);

        if (sala_bina != False):
            print(f"{mensagem}, mas não consegui achar.");
        
        else:
            print(f"Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.")
else:
    print("Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.")