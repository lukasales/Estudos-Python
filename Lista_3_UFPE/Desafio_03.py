sintomas = ["dor de cabeca", "insonia", "pesadelos", "suor frio" ,"visoes"];
comando = str(input());
pacientes = [];
nomes = [];
d = int(0);

while (comando != str("descobrir")):
    aluno = (comando.split(", "));
    pacientes = (aluno);
    check = True;
    k = [];

    while ((check == True)):

            for i in pacientes[1:]:

                if (i in sintomas):

                    if (i not in k):
                        d += int(1);

                check = False;
                k.append(i)
            
            else:

                if(d == int(5)):
                    nomes.append(pacientes[0]);

            d = int(0);
            comando = str(input());
else:
    aux_nome = len(nomes);
    j = int(1);
    msg_final = str();

    if (len(nomes) == int(0)):
        print("Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.");
    else:

        if("Max" in nomes):
            print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.");
        
            if(aux_nome > int(1)):
                print(f"Além dela, tem mais {(aux_nome - 1)} pessoa(s) na mira do Vecna!");
                verificador = True;

                while (verificador == True):

                    if (aux_nome > int(3)):
                        msg_final += (f"{nomes[j]}, ");
                        aux_nome -= int(1);
                        j += int(1);

                    elif(aux_nome > int(2)):
                        msg_final += (f"{nomes[j]} ");
                        aux_nome -= int(1);
                        j += int(1);

                    else:
                        if(len(nomes) > int(2)):
                            aux_nome -= int(1);
                            msg_final += (f"e {nomes[j]}");
                            print(f"Precisamos avisar {msg_final} para prepararem suas músicas favoritas.");

                        else:
                            aux_nome -= int(1);
                            msg_final += (f"{nomes[j]}");
                            print(f"Precisamos avisar {msg_final} para preparar sua música favorita.");
                        verificador = False

        else:
            aux_nome = len(nomes);
            j = int(0);

            if (aux_nome > int(1)):
                print (f"Tem {(len(nomes))} pessoa(s) na mira do Vecna!");
                verificador = True

                while (verificador == True):

                    if (aux_nome > int(2)):
                        msg_final += (f"{nomes[j]}, ");
                        aux_nome -= int(1);
                        j += int(1);

                    elif(aux_nome > int(1)):
                        msg_final += (f"{nomes[j]} ");
                        aux_nome -= int(1);
                        j += int(1);

                    else:
                        msg_final += (f"e {nomes[j]}");
                        print(f"Precisamos avisar {msg_final} para prepararem suas músicas favoritas.");
                        verificador = False

            else:
                print (f"Tem {(len(nomes))} pessoa(s) na mira do Vecna!");
                print(f"Precisamos avisar {nomes[0]} para preparar sua música favorita.");