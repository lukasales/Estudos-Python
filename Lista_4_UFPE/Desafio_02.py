chave = True;
chave_mar_podre = False;
chave_tropas_estrangeiras = False;
chave_mar_tropas = False;
identificador =  [];

def fatiador():
    identificador.extend(comando.split(" "));

def verificador ():
    global chave_mar_podre;
    global chave_mar_tropas;
    global chave_tropas_estrangeiras;

    for i in identificador:

        if (((i == str("crcrcrcrcr")) or (i == str("uuuuuuuoooooo")) or (i == str("ooooooeeeeeeee")) or (chave_mar_podre == True)) and (chave_tropas_estrangeiras == False)):
            
            if ((i == str("ppprrrrrooon")) or (i == str("tutututututututu")) or (i == str("eeeeeeeeoooooo"))):
                chave_mar_tropas = True;

            else:
                chave_mar_podre = True;
        
        elif (((i == str("ppprrrrrooon")) or (i == str("tutututututututu")) or (i == str("eeeeeeeeoooooo")) or (chave_tropas_estrangeiras == True)) and (chave_mar_podre == False)):
            
            if ((i == str("crcrcrcrcr")) or (i == str("uuuuuuuoooooo")) or (i == str("ooooooeeeeeeee"))):
                chave_mar_tropas = True;

            else:
                chave_tropas_estrangeiras = True;

while (chave == True):
    comando = str(input());
    
    fatiador();
    verificador ();

    if (chave_mar_tropas == True):
        print("A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!");

    else:

        if (chave_mar_podre == True):
            print("É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…");
        
        elif (chave_tropas_estrangeiras == True):
            print("São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??");

        else:
            print("Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.");
            chave = False;

    chave_mar_podre = False;
    chave_tropas_estrangeiras = False;
    chave_mar_tropas = False;
    identificador = [];