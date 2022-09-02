quant_frascos = int(input());
entradas = int(input());
elementos = [];
x = int(0);
frascos_usad = [];
frascos_usad_aux = [];
elementos_usad = [];
elementos_usad_aux = [];
elementos_usad_aux_msg = str();
check = True;


for i in range(0,entradas):
    comando = str(input());
    elementos.extend(comando.split(" "));

else:

    for i in range(0,len(elementos)):

        if ((i%2) != int(0)):
            elementos[i] = int(elementos[i]);
            frascos_usad.append(elementos[i]);
            elementos_usad.append(elementos[i - 1]);

    else:
    
        verificador = len(frascos_usad);
        verificador_aux = len(frascos_usad);

        while ((verificador_aux > int(0)) and (check == True)):
                
            if (check == True):

                for j in range(1, verificador+1):

                    frascos_usad_aux = frascos_usad[0:j];
                    elementos_usad_aux = elementos_usad[0:j];
                    x += frascos_usad_aux[j-1];

                    if (x == quant_frascos):
                        check = False;

                        for k in range(0,j):
                            elementos_usad_aux_msg += (f"{elementos_usad_aux[k]} ");
                
                else:
                    y = frascos_usad.pop(0);
                    frascos_usad.append(y);
                    y = elementos_usad.pop(0);
                    elementos_usad.append(y);
                    verificador_aux -= int(1);
                    x = int(0);

        else:
        
            if (check == False):
                print(f"Vencemos a batalha e a humanidade foi restaurada! {elementos_usad_aux_msg}foram usados para deszumbificar");

            else:
                print(f"Estou sentido algo estranho... será que também vou virar zumbi?");