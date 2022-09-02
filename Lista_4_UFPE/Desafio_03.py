# De 0 até 49 minusculas 0 = a 25 = z, 26 = a
# De 50 até 99 maisculas 50 = A 75 = Z, 76 = A
# Se o número for 100 = " "
#Se algum número não estiver no intervalo identificado pelas regras acima, não é possível traduzi-lo.

#fazer uma lista e uma função para split o primeiro input na lista, depois criar uma lista que vai usar o loop de repetição para traduzir.

#posso fazer a primeira condição verificar se tem algum número fora do intervalo, se não estiver ele roda o código normal, se tiver ele ja finalizar o código.

#a númeração segue o index

lista_numb = [];
lista_alfa_minu = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
lista_alfa_maius = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
chave = True;
mensagem_tradu = "";

def armazenador():
    lista_numb.extend((comando.split()));
    
    for i in range(len(lista_numb)):
        lista_numb[i] = int(lista_numb[i]);

def verificador():

    for i in lista_numb:
        global chave;
        
        if (i > (int(100))):
            chave = False; #condição para chamar o tradutor ou não.


def tradutor ():
    global mensagem_tradu;

    for i in lista_numb:
    
        if (i < (int(50))):

            if (i > int(25)):
                i = int(i - 26);

            mensagem_tradu += lista_alfa_minu[i];
        
        elif (i < (int(100))):
            i = int(i - 50);

            if (i > int(25)):
                i = int(i - 26);

            mensagem_tradu += lista_alfa_maius[i];
        
        else:
            mensagem_tradu += (" ");

comando = str(input());
armazenador ();
verificador ();

if (chave == True):
    tradutor();

else:
    mensagem_tradu = str("Infelizmente os números nao dizem nada");

print(mensagem_tradu);