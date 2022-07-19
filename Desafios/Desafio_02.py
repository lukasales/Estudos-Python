valor_x = int(input("Escreva um número para o ponto do eixo X? "))
valor_y = int(input("Escreva um número para o ponto do eixo Y? "))

if (valor_x == int(0) and valor_y == int(0)):
    print ("O ponto se encontra na origem!")

elif (valor_x >= int(0)):

    if(valor_y >= int(0)):
        print ("O ponto se encontra no eixo 1°!")

    else:
        print ("O ponto se encontra no eixo 4°!")

elif (valor_x <= int(0)):

    if (valor_y >= int (0)):
        print ("O ponto se encontra no eixo 2°!")

    else: 
        print ("O ponto se encontra no eixo 3°!")

else:
    print ("Esse valor não corresponde aos intervalos permitidos!")