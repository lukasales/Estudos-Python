palavra_aux = [];
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
senha = str(input());
qnt_pala = int(input());
chave_prin = False;

def f_fibonacci (n):
    if (n == int(0)):
        return  0;
    
    elif (n == int(1)):
        return 1;
    else:
        return f_fibonacci (n -1) + f_fibonacci (n - 2);

def f_fatorial (f):

    if (f <= int(0)):
        return 1;

    else:
        return f * f_fatorial(f-1);

for i in range(0,qnt_pala):
    palavra = str(input());
    palavra_aux.extend(palavra);
    poss_senha = str("");

    for j in palavra_aux:
        fibonacci_aux = [];
        fatorial_aux = [];
        index = alfabeto.index(j);

        for z in range(0, (index + 1)):
            fibonacci_aux.append(f_fibonacci(z));
    
        else:

            for z in range(0, (index)):
                fatorial_aux.append(f_fatorial(z));

            else:

                if (len(fibonacci_aux) == 0):
                    print("não entendi");
                
                elif ((index % 2) == int(0)):
                    
                    for k in range(0, len(fatorial_aux)):
                        index_aux = int(fibonacci_aux[k] + fatorial_aux[k]);

                        if ((index_aux > int(25))):
                            fator = int((index_aux/26));
                            index_aux -= int(26*(fator));
                            letra = alfabeto[index_aux];
                            poss_senha += str(letra);
                        
                        else:
                            letra = alfabeto[index_aux];
                            poss_senha += str(letra);

                else:
                    for k in range(0, len(fatorial_aux)):
                        index_aux = int(fibonacci_aux[k] * fatorial_aux[k]);
                    
                        if ((index_aux > int(25))):
                            fator = int((index_aux/26));
                            index_aux -= int(26*(fator));
                            letra = alfabeto[index_aux];
                            poss_senha += str(letra);
                        
                        else:
                            letra = alfabeto[index_aux];
                            poss_senha += str(letra);
    else:

        if (poss_senha == senha):
            chave_prin = True;

else:

    if (chave_prin == True):
        print("Achamos! Achamos a senha.");

    else:
        print("É... Temos que procurar mais.");