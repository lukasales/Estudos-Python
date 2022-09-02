numero = int(1);
lis_result = [];

while (numero == int(1)):
    repeticao = int(0);
    comando = str(input());
    repeticao = int(input());

    if (comando == str("S")):
        def soma ():
            x = int(input()); #1
            
            for i in range(1,repeticao):
                y = int(input()); #2
                x += int(y); #resultado

            else:
                lis_result.append(x);
        
        soma();

    elif (comando == str("sub")):
        def subtração ():
            x = int(input()); #1
            
            for i in range(1,repeticao):
                y = int(input()); #2
                x -= int(y); #resultado colocar valor absoluto

            else:
                lis_result.append(x);
        
        subtração();
    elif (comando == str("M")):
        def multiplicação ():
            x = int(input()); #1
            
            for i in range(1,repeticao):
                y = int(input()); #2
                x *= int(y); #resultado

            else:
                lis_result.append(x);
        
        multiplicação();
    elif (comando == str("D")):
        def divisão ():
            x = int(input()); #1
            
            for i in range(1,repeticao):
                y = int(input()); #2
                x /= int(y); #resultado

            else:
                lis_result.append(x);
        
        divisão();
    
    numero = int(input());
else:
    verificador = len(lis_result);

    for i in range(0,verificador):
        print(f"{lis_result[i]}");