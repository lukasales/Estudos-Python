contador = int(input());
chave = str("");

def verificador(sent, numb_abert, numb_fech):
    sent_aux = str("");
    sent_respo = str("");

    if (len(sent) <= int(0)):

        if (numb_abert == numb_fech):
            sent_respo = str("parênteses Aber iguais aos Fech");
        
        elif(numb_abert < numb_fech):
            sent_respo = str("parênteses Aber menores aos Fech");
        
        else:
            sent_respo = str("parênteses Aber maiores aos Fech");
        
        return sent_respo;

    else:
        sent_aux = sent[0];

        if (sent_aux == str("(")):
            numb_abert += int(1);

        elif (sent_aux == str(")")):
            numb_fech += int(1);
        
        sent.pop(0);
        return  verificador(sent, numb_abert, numb_fech);
        

while (contador > int(0)):
    sentenca = str(input());
    elementos_da_sentenca = [];
    elementos_da_sentenca.extend(sentenca);
    chave = verificador(elementos_da_sentenca, 0, 0);

    if (chave == str("parênteses Aber iguais aos Fech")):
        print(f"Essa sentença está com os parênteses balanceados, HOORAY!");
    
    elif (chave == str("parênteses Aber menores aos Fech")):
        print(f"A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la");
    else:
        print(f"A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la");

    contador -= int(1);