n = int(input())
acerto = int(0)
erro = int(0)

for i in range (n):
# casos com 0 e 1
    operacao = str(input())

    if (operacao == str("DEC")):
        binario = str(input())
        palpite_deci = int(input())
        valor = int(binario)
        binario_conver = int(0)
        x = len(str(binario))

        for i in range (x):
            resto_bina = int(valor%2)
            binario_conver += int(resto_bina * (2**i))
            valor = (valor // 10)
        
        else:

            if (palpite_deci == binario_conver):
                acerto += int(1)
        
            else:
                erro += int(1)
                print (f"Palpite Incorreto, o valor {binario} = {binario_conver}")
        
    elif (operacao == str("BIN")):
        resto_conver = str()
        decimal = int(input())
        decimal_aux = int(decimal)
        palpite_bina = str(input())

        if (decimal == int(0)):
            resto_conver = str("0")

            if (palpite_bina == resto_conver):
                acerto += int(1)
        
            else:
                erro += int(1)
                print (f"Palpite Incorreto, o valor {decimal} = {resto_conver}")
        
        else:

            while (decimal_aux > int(0)):
                resto_decim = int(decimal_aux%2)
                resto_conver += str(resto_decim)
                decimal_aux = int((decimal_aux - resto_decim)/2)
            
            else:
                
                if (palpite_bina == resto_conver[::-1]):
                    acerto += int(1)
            
                else:
                    erro += int(1)
                    print (f"Palpite Incorreto, o valor {decimal} = {resto_conver[::-1]}")

                    #problema está nos zeros a esquerda
else:
    
    resultado = int(acerto + erro)

    if (acerto > (resultado*0.5)):
        print ("Bazinga! Quem realizou esses cálculos foi o computador??")
    
    else:
        print ("Parece que realizar conversões em binário não é o seu forte")