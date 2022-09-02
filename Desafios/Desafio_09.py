nome = str(input("Nome do animal? "))
distancia = int(input(f"Qual a distância, em cm, que {nome} vai percorrer? "))
passos = int(input(f"Qual o tamanho dos passos, em cm, do {nome}? "))
num_passos = int(0)


while ((nome == "") or (distancia == 0) or passos == 0):
    print ("informações invalidas!")
    nome = str(input("Nome do animal? "))
    distancia = int(input(f"Qual a distância, em cm, que {nome} vai percorrer? "))
    passos = int(input(f"Qual o tamanho dos passos, em cm, do {nome}? "))

else:

    for i in range (0, distancia, passos):
        num_passos += int(1)

    print (f"{nome}, para percorrer a distância de {distancia}cm, ele precisa dar {num_passos}.")