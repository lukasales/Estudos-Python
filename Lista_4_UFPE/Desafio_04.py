lista_silabas = [];
lista_silabas_aux = [];
lista_silabas_verif_aux = [];
lista_silabas_hos = ["shi", "chi", "ko", "ku", "ya", "ma"];
lista_nomes_hos = ["shichi", "shichiko", "shichikoku", "shichikokuya", "shichikokuyama", "chiko", "chikoku", "chikokuya", "chikokuyama", "koku", "kokuya", "kokuyama", "kuya", "kuyama", "yama"];
check = False;
check_continuar = True;
check_palavra_toda = False;
x = int(0);
mensagem = "";

def fatiador(nome):
    global lista_silabas_aux;
    lista_silabas_aux_nome = [];
    silaba = "";
    lista_silabas_aux_nome.extend(nome);

    for i in lista_silabas_aux_nome:

        if ((i == str("a")) or (i == str("e")) or (i == str("i")) or (i == str("o")) or (i == str("u"))):
            silaba += str(i);
            lista_silabas_aux.append(silaba);
            silaba = "";
        
        else:
            silaba += str(i);

def verificador ():
    palavra_completa = "";
    check_palavra_toda_aux = True;
    global check_palavra_toda;
    global check;

    for i in lista_silabas_aux:

        if (i in lista_silabas_hos):

            if (i not in lista_silabas):
                lista_silabas.append(i);
                lista_silabas_verif_aux.append(i);
                check = True;
                palavra_completa += i;

            else:
                check_palavra_toda_aux = False;   
        
        else:
            check_palavra_toda = False;

    else:
        
        if ((palavra_completa in lista_nomes_hos) and (check_palavra_toda_aux == True)):
            check_palavra_toda = True;
    
def verificador_quant_silabas ():
    global x;
    verifi_silaba = "";

    for i in lista_silabas_aux:

        if (i in lista_silabas_verif_aux):
            
            if (i != verifi_silaba):
                verifi_silaba = i;
                x += int(1);

while (check_continuar == True):
    comando = str(input());
    fatiador(comando);
    verificador();
    verificador_quant_silabas();

    if (check == True):

        if (check_palavra_toda == False):

            if (x == int(1)):
                print(f"Lembrei! A sílaba {lista_silabas_verif_aux[0]} está no nome do hospital. Obrigada, Totoro!")
            
            else:
                contador = len(lista_silabas_verif_aux);
                
                for i in range(len(lista_silabas_verif_aux)):
                
                    if (contador > int(2)):
                        mensagem += str(f"{lista_silabas_verif_aux[i]}, ");

                    else:
                        if (contador > int(1)):
                            mensagem += str(f"{lista_silabas_verif_aux[i]}, ");
        
                        else:
                            mensagem += str(f"{lista_silabas_verif_aux[i]}");  

                    contador -= int(1);

                else:
                    print(f"Lembrei! As sílabas: {mensagem} estão no nome do hospital. Obrigada, Totoro!");   

        else:
             
            if (x > int(1)):
                print(f"A palavra {comando} está toda no nome do hospital. Acertou em cheio, Totoro!")

            else:
                print(f"Lembrei! A sílaba {lista_silabas_verif_aux[0]} está no nome do hospital. Obrigada, Totoro!")

    else: 
        print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.");

    lista_silabas_aux = [];
    lista_silabas_verif_aux = [];
    x = int(0);
    verif_continuar = int(0);
    check = False;
    mensagem = "";

    for i in lista_silabas:

        if (i in lista_silabas_hos):
            verif_continuar += int(1);

            if (verif_continuar == (len(lista_silabas_hos))):
                check_continuar = False;
        
            else: 
                check_continuar = True;
else:
    print("Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!");