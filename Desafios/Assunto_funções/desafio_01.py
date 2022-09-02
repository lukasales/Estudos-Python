from random import randint


print("inicio")

def jogodeazar ():
    num = randint(0,100);
    acerto = False;
    chute = int(input("Escola um número de 1 a 100: "));
    
    while (acerto == False):
        
        if (chute == num):
            print("Parabéns! Você acertou o número!");
            acerto = True;
        
        elif (chute > num):
            chute = int(input("Tente um número menor: "));
        
        else:
            chute = int(input("Tente um número maior: "));

jogodeazar();

print("Fim");
