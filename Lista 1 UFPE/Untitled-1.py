seu_nome = input("nome?")
seus_pontos_vida = int(12)
seu_ataque = int(input("ataque?"))
sua_defesa = int(12)
nome_entidade = input("nome entidade?")
defesa_entidade = int(input("defesa? "))
pontos_vida_entidade = int(input("vida entidade?"))
fraqueza_entidade = input()
resistencia_entidade = input()
acao_2 = input("acao 1?")
dano_ataque = int(12)
dano_ataque_entidade = dano_ataque
sua_resistencia = "avc"
sua_fraqueza = "ads"

if ((acao_2 == "Ataque Físico") or ((acao_2 == "Agi" and sua_fraqueza != "fogo" ) or (acao_2 == "Bufu" and sua_fraqueza != "gelo") or (acao_2 == "Zio" and sua_fraqueza != "eletricidade")) or (sua_fraqueza == "nao tem") or (sua_resistencia == "nao tem")):
  
  if ((dano_ataque_entidade > 0)):

    if((dano_ataque_entidade < 0)):
        dano_ataque_entidade *= int(-1)
  print (seus_pontos_vida) 
  seus_pontos_vida -= int(dano_ataque_entidade)
  print (seus_pontos_vida)
  if ((seus_pontos_vida > 0)):  
      print (f"{nome_entidade} usou {acao_2} e causou {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

  else:
    seus_pontos_vida = int(0)
    print (f"{nome_entidade} usou {acao_2} e causou {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

else:
  resistencia_2 = False
  dano_ataque_resistencia_entidade = int((dano_ataque_entidade - sua_defesa)*0.5)

  if (((acao_2 == "Agi" and sua_resistencia == "fogo" ) or (acao_2 == "Bufu" and sua_resistencia == "gelo") or (acao_2 == "Zio" and sua_resistencia == "eletricidade"))):
    resistencia_2 = True

    if ((dano_ataque_resistencia_entidade > 0)):
      pontos_vida_entidade -= int(dano_ataque_resistencia_entidade)
      
    else:
      dano_ataque_resistencia_entidade *= int(-1)
      pontos_vida_entidade -= int(dano_ataque_resistencia_entidade)

    if ((seus_pontos_vida > 0)):  
        print (f"{nome_entidade} usou {acao_2}, mas acertou uma resistência, portanto causou apenas {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

    else:
      seus_pontos_vida = int(0)
      print (f"{nome_entidade} usou {acao_2}, mas acertou uma resistência, portanto causou apenas {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

    if pontos_vida_entidade == int(0):
      print (f"Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…")

  else:
    critico_entidade_2 = False
    dano_ataque_magico_entidade = int((seu_ataque - defesa_entidade)*1.7)

    if (((acao_2 == "Agi" and sua_fraqueza == "fogo" ) or (acao_2 == "Bufu" and sua_fraqueza == "gelo") or (acao_2 == "Zio" and sua_fraqueza == "eletricidade"))):
      critico_entidade_2 = True
      if ((dano_ataque_magico_entidade > 0)):
          seus_pontos_vida -= int(dano_ataque_magico_entidade)
      
      else:
        dano_ataque_magico_entidade *= int(-1)
        seus_pontos_vida -= int(dano_ataque_magico_entidade)

      if ((seus_pontos_vida > 0)):  
        print (f"Vixe! {nome_entidade} usou {acao_2} e acertou sua fraqueza! A magia causou {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

      else:
        seus_pontos_vida = int(0)
        print (f"Vixe! {nome_entidade} usou {acao_2} e acertou sua fraqueza! A magia causou {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")
    
      if seus_pontos_vida == int(0):
        print (f"Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…")

      else:
        if critico_entidade_2:
          numero_turno = int(3)
          print (f"Turno: {numero_turno}")
          print (f"{seu_nome} teve sua fraqueza em {acao_2} acertada, portanto não poderá agir.")
          if seus_pontos_vida == int(0):
            print (f"Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…")

          else: 
            print ("Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")

    else:
        acao_3 = str(input())
        numero_turno = int(3)
        print (f"Turno: {numero_turno}")

        if ((acao_3 == "Ataque Físico") or ((acao_3 == "Agi" and fraqueza_entidade != "fogo") or (acao_3 == "Bufu" and fraqueza_entidade != "gelo") or (acao_3 == "Zio" and fraqueza_entidade != "eletricidade")) or (fraqueza_entidade == "nao tem") or (resistencia_entidade == "nao tem")):
        
            if ((dano_ataque > 0)):
                pontos_vida_entidade -= int(dano_ataque)
            
            else:
                dano_ataque *= int(-1)
                pontos_vida_entidade -= int(dano_ataque)

            if ((pontos_vida_entidade > 0)):
                print (f"{seu_nome} usou {acao_3} e causou {dano_ataque} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
                
            else:
                pontos_vida_entidade = int(0)
                print (f"{seu_nome} usou {acao_3} e causou {dano_ataque} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
            
        else:
            resistencia_3 = False
            dano_ataque_resistencia = int((seu_ataque - defesa_entidade)*0.5)

            if (((acao_3 == "Agi" and resistencia_entidade == "fogo" ) or (acao_3 == "Bufu" and resistencia_entidade == "gelo") or (acao_3 == "Zio" and resistencia_entidade == "eletricidade"))):
                resistencia_3 = True

            if ((dano_ataque_resistencia > 0)):
                pontos_vida_entidade -= int(dano_ataque_resistencia)
            
            else:
                dano_ataque_resistencia *= int(-1)
                pontos_vida_entidade -= int(dano_ataque_resistencia)

            if ((pontos_vida_entidade > 0)):  
                print (f"{seu_nome} usou {acao_3}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

            else:
                pontos_vida_entidade = int(0)
                print (f"{seu_nome} usou {acao_3}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
                
            if pontos_vida_entidade == int(0):
                print ("Vitória! Parece que o Nahobino São João reinará nesse solstício!")

            else:

                meu_critico_3 = False #se for falso ele vai continuar o programa
                dano_ataque_magico = int((seu_ataque - defesa_entidade)*1.7)

                if (((acao_3 == "Agi" and fraqueza_entidade == "fogo" ) or (acao_3 == "Bufu" and fraqueza_entidade == "gelo") or (acao_3 == "Zio" and fraqueza_entidade == "eletricidade"))):
                    meu_critico = True

                    if ((dano_ataque_magico > 0)):
                        pontos_vida_entidade -= int(dano_ataque_magico)
            
                    else:
                        dano_ataque_magico *= int(-1)
                        pontos_vida_entidade -= int(dano_ataque_magico)

                    if ((pontos_vida_entidade > 0)):  
                        print (f"Isso! {seu_nome} usou {acao_3} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

                    else:
                        pontos_vida_entidade = int(0)
                        print (f"Isso! {seu_nome} usou {acao_3} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")
                    
                if pontos_vida_entidade == int(0):
                    print ("Vitória! Parece que o Nahobino São João reinará nesse solstício!")

                else:
                    print ("Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")