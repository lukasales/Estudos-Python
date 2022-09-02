from operator import truediv

seu_nome = input("nome?")
seu_ataque = int(input("ataque?"))
nome_entidade = input("nome entidade?")
defesa_entidade = int(input("defesa? "))
pontos_vida_entidade = int(input("vida entidade?"))
fraqueza_entidade = input()
resistencia_entidade = input()
acao_1 = input("acao 1?")

#dano = False #se for falso ele vai multiplicar o dano por -1
meu_critico_1 = False #se for falso ele vai continuar o programa
dano_ataque_magico = int((seu_ataque - defesa_entidade)*1.7)

if (((acao_1 == "Agi" and fraqueza_entidade == "fogo" ) or (acao_1 == "Bufu" and fraqueza_entidade == "gelo") or (acao_1 == "Zio" and fraqueza_entidade == "eletricidade"))):
    meu_critico_1 = True
    if ((dano_ataque_magico > 0)):
        pontos_vida_entidade -= int(dano_ataque_magico)
    
        if ((pontos_vida_entidade > 0)):  
            print (f"Isso! {seu_nome} usou {acao_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

        else:
            pontos_vida_entidade = int(0)
            print (f"Isso! {seu_nome} usou {acao_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
    
    elif ((dano_ataque_magico < 0)):
        dano_ataque_magico *= int(-1)
        pontos_vida_entidade -= int(dano_ataque_magico)

        if ((pontos_vida_entidade > 0)):  
            print (f"Isso! {seu_nome} usou {acao_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

        else:
            pontos_vida_entidade = int(0)
            print (f"Isso! {seu_nome} usou {acao_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
if meu_critico_1:
    print (f"aaaaaaaaaaaa{nome_entidade} teve sua fraqueza em {fraqueza_entidade} acertada, portanto não poderá agir.")
    if pontos_vida_entidade == int(0):
        print ("Vitória! Parece que o Nahobino São João reinará nesse solstício!")
else:
    print (f"Isso! {seu_nome} usou {acao_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
    acao_2 = input("acao 2?")
    if meu_critico:
        print ("deu certo", acao_2)
    else:
        print ("entendi")
        print (meu_critico)
        print(acao_2)