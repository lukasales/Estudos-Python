comando = str(input())
lista_suspeitos = [];
lista_suspeitos = comando.split(',')

while ((len(lista_suspeitos) > int(1))):
    comando = str(input());
    
    if(comando == str("Não encontrei nada no primeiro suspeito")):
        lista_suspeitos.pop(0);

    elif(comando == str("O último da lista está limpo")):
        lista_suspeitos.pop();
    
    elif(comando == str("Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita")):

        if ((len(lista_suspeitos)%2 == int(0))):
            meio = int((len(lista_suspeitos)/2));
            lista_suspeitos.pop(meio);


        else:
            meio = int(((len(lista_suspeitos)+1)/2)-1);
            lista_suspeitos.pop(meio);

    
    elif(comando == str("Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:")):
        valor = int(input());
        lista_suspeitos.pop(valor);
    
    elif (comando == str("Acho que temos mais uma opção a ser analisada…")):
        nome = str(input());
        lista_suspeitos.append(nome);
    
    else:
        print("Isso não estava no combinado, a lista vai permanecer do mesmo jeito");
else: 
    
    print(f"Acho que encontramos o suspeito. O seu nome é {lista_suspeitos[0]}, vamos salvar o Sam!");