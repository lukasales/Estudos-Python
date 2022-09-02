from sys import intern


Temperatura = int(30)
Fome = str("Com fome")
Internet = int(0)

acao = str(input())

while (acao != "parar"):

    if (acao == "ir para o grad"):
        Temperatura -= int(5)
        Internet += int(300)
    
    elif (acao == "sair para a rua"):
        Temperatura += int(5)
    
    elif (acao == "comer uma quentinha"):
        Fome = str("Sem fome")
    
    elif (acao == "conectar no wifi"):
        Internet += int(100)
    
    else: 
        print ("Entrada inválida")

    acao = str(input())

else: 
    
    perfeito = False
    if (Temperatura >= int(30)):
        print ("A temperatura aqui não está agradável")
    
    elif (Temperatura <= int(25)):
        print ("Agora sim, está aconchegante")
        perfeito = True

    if (Fome == str("Com fome")):
        print ("Meu corpo precisa de comida")
        perfeito = False

    if (Internet < int(100)):
        print ("Essa conexão está horrível")
        perfeito = False
    
if ((perfeito == True) and (Internet >= int(300))):
    print("Finalmente um lugar preciso para mim!")