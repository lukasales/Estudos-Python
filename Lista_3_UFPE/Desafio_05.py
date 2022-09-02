resultado_1 = [];
resultado_1_aux = [];
resultado_2 = [];
pontuacao_ant_inter = [];
pontuacao_dps_inter = [];
comando = input();
resultado_1 = comando.split(" ");
resultado_1_aux = comando.split(" ");
comando = input();
resultado_2 = (comando.split(" "));
verificador = len(resultado_2);
verifi_aux = int(0);
total_soma_pon = int(0);
total_soma_pon_aux = int(0);

for i in range(0,verificador):
    
    if (resultado_2[i] == str("1")):

        if (resultado_1[i] == str("V")):
            resultado_1[i] = str("E");
            print(f"O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.");

        elif (resultado_1[i] == str("E")):
            resultado_1[i] = str("D");
            print(f"O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.");

        else:
            resultado_1[i] = str("D");
            print(f"O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!");
else:

    for j in range(0,verificador,4):
        soma_pon = int(0);
        soma_pon_aux = int(0);

        for k in range(0,4):

            if (resultado_1[verifi_aux] == str("V")):
                soma_pon += int(3);

            elif (resultado_1[verifi_aux] == str("E")):
                soma_pon += int(1);

            else:
                soma_pon += int(0);

            if (resultado_1_aux[verifi_aux] == str("V")):
                    soma_pon_aux += int(3);

            elif (resultado_1_aux[verifi_aux] == str("E")):
                soma_pon_aux += int(1);

            else:
                soma_pon_aux += int(0);

            verifi_aux += int(1);

        else:
            pontuacao_dps_inter.append(soma_pon);
            pontuacao_ant_inter.append(soma_pon_aux);
            total_soma_pon += int(soma_pon);
            total_soma_pon_aux += int(soma_pon_aux);

    else:

        for i in range(0,3):
            
            if (pontuacao_dps_inter[i] == int(7)):
                print(f"A pontuação na {(i + 1)}ª fatia de 4 jogos está dentro do planejado.");
            
            elif (pontuacao_dps_inter[i] > int(7)):
                print(f"A pontuação na {(i + 1)}ª fatia de 4 jogos está com uma gordurinha de {(pontuacao_dps_inter[i] - 7)} pontos.");
            
            else:
                print(f"A pontuação na {(i + 1)}ª fatia de 4 jogos está abaixo da planejada em {(7 - pontuacao_dps_inter[i])} pontos.");
            
        else:

            if (abs(total_soma_pon_aux - total_soma_pon) > int(0)):
                print(f"A maldição do sapo fez o Vascão perder {abs(total_soma_pon_aux - total_soma_pon)} pontos. Um número preocupante, que pode fazer diferença.");
            
            else:
                print(f"A maldição parece que não teve impacto relevante! Não houve nenhuma perda de pontos.");
            
            if (total_soma_pon >= int(21)):
                print(f"Na reta final do campeonato, o Vasco garantiu um total de {total_soma_pon} pontos, com {resultado_1.count('V')} vitórias, {resultado_1.count('E')} empates e {resultado_1.count('D')} derrotas, e alcançou o tão esperado acesso. O Clube do Fomento Corporal vibra num SJ lotado!")
            
            else:
                print(f"Na reta final do campeonato, o Vasco fez somente {total_soma_pon} pontos, com {resultado_1.count('V')} vitórias, {resultado_1.count('E')} empates e {resultado_1.count('D')} derrotas, e não conseguiu o acesso. Mais um ano de série B e sofrimento. Mob, o clube e a torcida estão completamente desolados.")