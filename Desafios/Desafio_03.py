print("Descubra que tipo de triângulo é pelos valores dos seus lados! \nDigite 3 valores!")

lado_1 = int(input("Digite o valor do primeiro lado do triângulo: "))
lado_2 = int(input("Digite o valor do segundo lado do triângulo: "))
lado_3 = int(input("Digite o valor do terceiro lado do triângulo: "))

if ((lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1)):

    if ((lado_1 == lado_2)):
    
        if ((lado_2 == lado_3)):
            print ("Esse triângulo equilatero!")

        if ((lado_2 != lado_3)):
            print ("Esse triângulo é isóceles!")

    elif ((lado_1 != lado_2) and (lado_1 != lado_3) and (lado_2 != lado_3)):
        print ("Esse triângulo é escaleno!")

elif(lado_1 <= int(0) or (lado_2 <= int(0)) or (lado_3 <= int(0))):
    print("Esses valores não obedece a lei de existência dos triângulos 0\nDigite valores positivos e diferentes de 0!")

else: 
    print("Esses valores não obedece a lei de existência dos triângulos \nDigite valores que estejam de acordo com a regra: Lx + Ly > Lz!")