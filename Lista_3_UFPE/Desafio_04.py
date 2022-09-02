nomes = [];
nomes_aux = [];
soma_palav = int(0);
soma_palav_rep = int(0);
nomes_n_repet = [];
nomes_repet = [];
x = int(0);
y = int(0);

for i in range(0,10,1):
    palavras = str(input());
    nomes.append(palavras);

else: 
    
    for i in nomes:

        if(i not in nomes_aux):
            nomes_aux.append(i);
            soma_palav += len(nomes_aux[x])
            x += int(1);

        else:
            
            if (i not in nomes_repet):
                nomes_repet.append(i);
                soma_palav_rep += len(nomes_repet[y])
                y += int(1);

    else:
        
        for j in nomes_aux:

            if (j not in nomes_repet):
                nomes_n_repet.append(j);
                
        else:
            verificador = len(nomes_n_repet);
            print(f"As palavras sao:");

            for z in range(verificador):
                print(f"{nomes_n_repet[z]}")
            
            else:
                print(f"A soma do tamanho das palavras é: {soma_palav - soma_palav_rep}");
                print("Estou impressionado, você me venceu, pode ir embora...");