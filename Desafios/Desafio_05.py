nome = str(input("Qual é seu nome? "))
resp = str(input("Você quer testar sua sorte em um jogo? "))

while ((resp != "sim") and (resp != "não")):
    print (f"{nome}, essa resposta é inválida!")
    resp = str(input("Você quer testar sua sorte em um jogo? "))

else:

    if ((resp == "não")):
        print (f"{nome}, que pena, deixa pra próxima!")
    
    else: 

        from random import randint

        num = randint (0, 100)

        print(f"Certo vamos jogar \n {nome}! que a sorte esteja com você")
        resp1 = int(input("Escolha um número de 0 à 100: "))

        while (resp1 != num):

            if (resp1 > num):
                print (f"{nome}! foi quase, escolha um número menor")
                resp1 = int(input("Escolha um número de 0 à 100: "))
            
            else: 
                print (f"{nome}! foi quase, escolha um número maior")
                resp1 = int(input("Escolha um número de 0 à 100: "))
        
        else: 
            print (f"{nome}! Boa você acertou! \nO número era {num}")