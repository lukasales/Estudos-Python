seu_nome = input("nome?")
seu_ataque = int(input("ataque?"))
nome_entidade = input("nome entidade?")
defesa_entidade = int(input("defesa? "))
pontos_vida_entidade = int(input("vida entidade?"))
fraqueza_entidade = input()
resistencia_entidade = input()
acao_1 = input("acao 1?")

#dano = False #se for falso ele vai multiplicar o dano por -1
resistencia_1 = False #se for falso ele vai continuar o programa
dano_ataque_resistencia = int((seu_ataque - defesa_entidade)*0.5)

if (((acao_1 == "Agi" and resistencia_entidade == "fogo" ) or (acao_1 == "Bufu" and resistencia_entidade == "gelo") or (acao_1 == "Zio" and resistencia_entidade == "eletricidade"))):
    resistencia_1 = True
    if ((dano_ataque_resistencia > 0)):
    
        if (dano_ataque_resistencia < 0):
            dano_ataque_resistencia *= int(-1)
    print(pontos_vida_entidade)
    pontos_vida_entidade -= int(dano_ataque_resistencia)
    print(pontos_vida_entidade)

    if ((pontos_vida_entidade > 0)):  
        print (f"{seu_nome} usou {acao_1}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

    else:
        pontos_vida_entidade = int(0)
        print (f"{seu_nome} usou {acao_1}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
if pontos_vida_entidade == int(0):
        print ("Vitória! Parece que o Nahobino São João reinará nesse solstício!")
else:
    print ("Acertou")