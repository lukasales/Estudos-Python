critico = False

if (acao_1 == "Agi" and fraqueza_entidade == "fogo" ) or (acao_1 == "Bufu" and fraqueza_entidade == "gelo") or (acao_1 == "Zio" and fraqueza_entidade == "eletricidade"):
    critico = True
    if vida_entidade <= 0:
        vida_entidade = 0

if jggk:
    print
else:
    if critico == True:
        print
    else: 

if critico:  # se for verdade ele printa isso
    print ("")

else: #se for falso ele continua o outro turno