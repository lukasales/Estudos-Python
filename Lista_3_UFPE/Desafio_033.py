sintomas = ["dor de cabeça", "insônia", "pesadelos", "suor frio" ,"visões"];
comando = str();
pacientes = [];
nomes = [];
d = int(1);
j = int(0);

while (comando != str("descobrir")):
    comando = str(input());
    aluno = (comando.split(", "));
    pacientes = (aluno);
    teste = (len(sintomas)-1);

    while (teste > int(0)):


        if (pacientes[d] == sintomas[j]):
            check = True;
            nomes = (pacientes[0]);
            teste -= int(1);
            d += int(1);
        
        else:         
            j += int(1);

else:
    print(nomes)
