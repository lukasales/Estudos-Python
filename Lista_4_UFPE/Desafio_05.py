tempo = int(0);
tempo_aux = int(0);
total_gorjetas = int(10);

def fun_servicos(servico):
    nome_servico = str("");

    if (tempo < int(120)):

        if (servico == str("pedras")):
            nome_servico = str("Pedras Quentes");
        
        elif (servico == str("pes")):
            nome_servico = str("Massagem nos Pes");
        
        elif (servico == str("refeicao")):
            nome_servico = str("Servir Refeicao");
        
        elif (servico == str("completa")):
            nome_servico = str("Massagem Completa");
        
        else:
            nome_servico = str("Não existe");

    else:
            nome_servico = str("Não existe");
                
    return nome_servico;

def fun_tempo(nome_servico_aux):
    tempo_aux = int(0);

    if (tempo < int(120)):

        if (nome_servico_aux == str("Pedras Quentes")):
            tempo_aux += int(20);

        elif (nome_servico_aux == str("Massagem nos Pes")):
            tempo_aux += int(30);

        elif (nome_servico_aux == str("Servir Refeicao")):
            tempo_aux += int(15);
        
        elif (nome_servico_aux == str("Massagem Completa")):
            tempo_aux += int(50);
        
        else:
            tempo_aux += int(5);

    return tempo_aux;

def fun_gorjeta(nome_servico_aux,tempo_aux,total_gorjetas_aux):
    gorjetas = int(0);

    if (nome_servico == str("Pedras Quentes")):
        gorjetas += int((((tempo_aux + total_gorjetas_aux)/2)));

    elif (nome_servico == str("Massagem nos Pes")):

        if ((total_gorjetas_aux) % 2 == 0):
            gorjetas += int(abs(((total_gorjetas_aux%7)*6)));
        
        else:
            gorjetas += int(abs(((total_gorjetas_aux%7)**2)));

    elif (nome_servico == str("Servir Refeicao")):

        if (((total_gorjetas_aux % 10) == 0)):
            gorjetas += int(5);

        while ((total_gorjetas_aux % 10) != 0):
            total_gorjetas_aux += int(1);
            gorjetas += int(1);
        
    elif (nome_servico == str("Massagem Completa")):
        total_gorjetas_temp = str(total_gorjetas);
        gorjeta_temp = int(0);

        for i in total_gorjetas_temp:
            gorjeta_temp += int(i);
        
        else:
            gorjetas = int(gorjeta_temp);

    return gorjetas;
    
while ((tempo < int(120)) and (total_gorjetas < int(50))):
    comando = str(input());
    nome_servico = fun_servicos(comando);
    tempo_aux += fun_tempo(nome_servico);
    total_gorjetas += fun_gorjeta(nome_servico,tempo,total_gorjetas);
    tempo = tempo_aux;
    
    if(nome_servico != str("Não existe")):
        print(f"Voce concluiu o servico de {nome_servico} e agora possui {total_gorjetas} gorjetas.");
    
    else:
        print(f"O cliente fez voce perder tempo, voce ainda possui {total_gorjetas} gorjetas.");

else:

    if (total_gorjetas >= int(50)):
        print(f"Você acumulou {total_gorjetas} gorjetas, com essa quantidade voce conseguira comprar sua passagem de saida e salvar seus pais.");
    
    else:
        print(f"Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.");