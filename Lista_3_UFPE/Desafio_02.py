nome = str(input());
quantidade = int(input());
filmes = [];
notas = [];

while (quantidade > int(0)):
    quantidade -= int(1);
    filme = input().split(" -");
    filme[1] = float(filme[1])
    filmes.append(filme[0]);
    notas.append(filme[1]);

else:
    def shortBubbleSort(notas):
        mudar = True;
        verificador = int(len(notas)-1);

        while ((verificador > 0) and (mudar == True)):
            mudar = False;

            for i in range(verificador):

                if notas[i]>notas[i+1]:
                    mudar = True;
                    temp_film = filmes[i];
                    filmes[i] = filmes[i+1];
                    filmes[i+1] = temp_film;
                    temp_nota = notas[i];
                    notas[i] = notas[i+1];
                    notas[i+1] = temp_nota;
                
            verificador -= int(1);
    shortBubbleSort(notas);
    filmes.reverse();
    notas.reverse();
    verificador = int(len(notas));

    if (nome == str("Bonna")):
        print("Os filmes sugeridos por Bonna são:");
    
    else: 
        print("Os filmes sugeridos por João são:");
    
    for j in range(verificador):
        print(f"{filmes[j]} - {notas[j]}");

#def shortBubbleSort(filmes):
#    mudar = True
#    verificador = len(filmes)-1
#    while verificador > 0 and mudar:
#       mudar = False
#       for i in range(verificador):
#           if filmes[i]>filmes[i+1]:
#               mudar = True
#               temp_nota = filmes[i]
#               filmes[i] = filmes[i+1]
#               filmes[i+1] = temp_nota
#       verificador = verificador-1
#
#filmes=[20,30,40,90,50,60,70,80,100,110]
#shortBubbleSort(filmes)
#print(filmes)
#
#isso é a estrutura para ordenar, nesse caso so vou precisar trocar os valores e adicionar tbm novas váriaveis na linha 9 ao 11, pois como vai ser uma string seguida de um número, será necessário mover a string junto com o numero E NA LINHA 10, SERA + 2 E NÃO + 1 

#outra alternativa de converter os valores
#quantidade -= int(1);
#aux = input().split("-");
#filme = aux[0];
#nota = float(aux[1]);
#filmes.append(filme);
#filmes.append(nota);