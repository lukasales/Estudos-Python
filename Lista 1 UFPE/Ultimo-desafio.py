seus_pontos_vida = int(input())
seu_ataque = int(input())
sua_defesa = int(input())
sua_fraqueza = str(input())
sua_resistencia = str(input())

nome_entidade = str(input())
pontos_vida_entidade = int(input())
ataque_entidade = int(input())
defesa_entidade = int(input())
fraqueza_entidade = str(input())
resistencia_entidade = str(input())

seu_nome = str("São João")
dano_ataque = int(seu_ataque - defesa_entidade)
dano_ataque_magico = int((dano_ataque)*1.7)
dano_ataque_resistencia = int((seu_ataque - defesa_entidade)*0.5)

dano_ataque_entidade = int(ataque_entidade - sua_defesa)
dano_ataque_magico_entidade = int((dano_ataque_entidade)*1.7)
dano_ataque_resistencia_entidade = int((dano_ataque_entidade)*0.5)

acao_1 = str(input())
numero_turno = int(1)
print (f"Turno: {numero_turno}")

meu_critico_1 = False
resistencia_1 = False
acao1 = False
acao2 = False
resistencia_2 = False
critico_entidade_2 = False
acao3 = False
resistencia_3 = False
meu_critico_3 = False 

if ((acao_1 == "Ataque Físico") or (acao_1 == "Agi" and (resistencia_entidade != "fogo" and fraqueza_entidade != "fogo")) or (acao_1 == "Bufu" and (resistencia_entidade != "gelo" and fraqueza_entidade != "gelo")) or (acao_1 == "Zio" and (resistencia_entidade != "eletricidade" and fraqueza_entidade != "eletricidade"))):
  acao1 = True

  if ((dano_ataque > 0)):
    pontos_vida_entidade -= int(dano_ataque)

  else:
    dano_ataque *= int(-1)
    pontos_vida_entidade -= int(dano_ataque)

  if ((pontos_vida_entidade > 0)):  
      print (f"{seu_nome} usou {acao_1} e causou {dano_ataque} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

  else:
    pontos_vida_entidade = int(0)
    print (f"{seu_nome} usou {acao_1} e causou {dano_ataque} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

if (acao1 == False):

  if (((acao_1 == "Agi" and resistencia_entidade == "fogo" ) or (acao_1 == "Bufu" and resistencia_entidade == "gelo") or (acao_1 == "Zio" and resistencia_entidade == "eletricidade"))):
    resistencia_1 = True

    if ((dano_ataque_resistencia > 0)):
      pontos_vida_entidade -= int(dano_ataque_resistencia)
      
    else:
      dano_ataque_resistencia *= int(-1)
      pontos_vida_entidade -= int(dano_ataque_resistencia)

    if ((pontos_vida_entidade > 0)):  
      print (f"{seu_nome} usou {acao_1}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

    else:
      pontos_vida_entidade = int(0)
      print (f"{seu_nome} usou {acao_1}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

if (resistencia_1 == False):

  if (((acao_1 == "Agi" and fraqueza_entidade == "fogo" ) or (acao_1 == "Bufu" and fraqueza_entidade == "gelo") or (acao_1 == "Zio" and fraqueza_entidade == "eletricidade"))):
    meu_critico_1 = True

    if ((dano_ataque_magico > 0)):
        pontos_vida_entidade -= int(dano_ataque_magico)
    
    else:
      dano_ataque_magico *= int(-1)
      pontos_vida_entidade -= int(dano_ataque_magico)

    if ((pontos_vida_entidade > 0)):  
      print (f"Isso! {seu_nome} usou {acao_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

    else:
      pontos_vida_entidade = int(0)
      print (f"Isso! {seu_nome} usou {acao_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque_magico} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.")

if ((pontos_vida_entidade > 0) and (meu_critico_1 == True)):
  numero_turno = int(2)
  print (f"Turno: {numero_turno}")
  print (f"{nome_entidade} teve sua fraqueza em {fraqueza_entidade} acertada, portanto não poderá agir.")

  if (pontos_vida_entidade > int(0)):

    acao_3 = str(input())
    numero_turno = int(3)
    print (f"Turno: {numero_turno}")

    if ((acao_3 == "Ataque Físico") or (acao_3 == "Agi" and (resistencia_entidade != "fogo" and fraqueza_entidade != "fogo")) or (acao_3 == "Bufu" and (resistencia_entidade != "gelo" and fraqueza_entidade != "gelo")) or (acao_3 == "Zio" and (resistencia_entidade != "eletricidade" and fraqueza_entidade != "eletricidade"))):
      acao3 = True

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
        
    if(acao3 == False):

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

    if (resistencia_3 == False):    

      if (((acao_3 == "Agi" and fraqueza_entidade == "fogo" ) or (acao_3 == "Bufu" and fraqueza_entidade == "gelo") or (acao_3 == "Zio" and fraqueza_entidade == "eletricidade"))):
        meu_critico_3 = True

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

if (pontos_vida_entidade <= int(0)):
  print ("Vitória! Parece que o Nahobino São João reinará nesse solstício!")

elif (pontos_vida_entidade > int(0) and seus_pontos_vida > int(0) and (acao3 == True or resistencia_3 == True or meu_critico_3 == True)):
  print ("Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")

else:

  if ((acao1 == True or resistencia_1 == True)):
    
    acao_2 = str(input())
    numero_turno = int(2)
    print (f"Turno: {numero_turno}")

    if ((acao_2 == "Ataque Físico") or (acao_2 == "Agi" and (sua_resistencia != "fogo" and sua_fraqueza != "fogo")) or (acao_2 == "Bufu" and (sua_resistencia != "gelo" and sua_fraqueza != "gelo")) or (acao_2 == "Zio" and (sua_resistencia != "eletricidade" and sua_fraqueza != "eletricidade"))):
      acao2 = True
      
      if ((dano_ataque_entidade > 0)):
        seus_pontos_vida -= int(dano_ataque_entidade)

      else:
        dano_ataque_entidade *= int(-1)
        seus_pontos_vida -= int(dano_ataque_entidade)

      if ((seus_pontos_vida > 0)):  
          print (f"{nome_entidade} usou {acao_2} e causou {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

      else:
        seus_pontos_vida = int(0)
        print (f"{nome_entidade} usou {acao_2} e causou {dano_ataque_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

    if (acao2 == False):

      if (((acao_2 == "Agi" and sua_resistencia == "fogo" ) or (acao_2 == "Bufu" and sua_resistencia == "gelo") or (acao_2 == "Zio" and sua_resistencia == "eletricidade"))):
        resistencia_2 = True

        if ((dano_ataque_resistencia_entidade > 0)):
          seus_pontos_vida -= int(dano_ataque_resistencia_entidade)
          
        else:
          dano_ataque_resistencia_entidade *= int(-1)
          seus_pontos_vida -= int(dano_ataque_resistencia_entidade)

        if ((seus_pontos_vida > 0)):  
            print (f"{nome_entidade} usou {acao_2}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

        else:
          seus_pontos_vida = int(0)
          print (f"{nome_entidade} usou {acao_2}, mas acertou uma resistência, portanto causou apenas {dano_ataque_resistencia_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

    if (resistencia_2 == False):

      if (((acao_2 == "Agi" and sua_fraqueza == "fogo" ) or (acao_2 == "Bufu" and sua_fraqueza == "gelo") or (acao_2 == "Zio" and sua_fraqueza == "eletricidade"))):
        critico_entidade_2 = True

        if ((dano_ataque_magico_entidade > 0)):
            seus_pontos_vida -= int(dano_ataque_magico_entidade)
        
        else:
          dano_ataque_magico_entidade *= int(-1)
          seus_pontos_vida -= int(dano_ataque_magico_entidade)

        if ((seus_pontos_vida > 0)):  
          print (f"Vixe! {nome_entidade} usou {acao_2} e acertou sua fraqueza! A magia causou {dano_ataque_magico_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

        else:
          seus_pontos_vida = int(0)
          print (f"Vixe! {nome_entidade} usou {acao_2} e acertou sua fraqueza! A magia causou {dano_ataque_magico_entidade} de dano em {seu_nome} que agora tem {seus_pontos_vida} de vida.")

      if ((seus_pontos_vida > int(0)) and (critico_entidade_2 == True)):
        acao_3 = str(input())
        numero_turno = int(3)
        print (f"Turno: {numero_turno}")
        print (f"{seu_nome} teve sua fraqueza em {sua_fraqueza} acertada, portanto não poderá agir.")

  if (seus_pontos_vida <= int(0)):
    print (f"Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…")

  elif (pontos_vida_entidade > int(0) and seus_pontos_vida > int(0) and critico_entidade_2 == True):
    print ("Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")

  else:
          
    if ((acao2 == True or resistencia_2 == True)):

      acao_3 = str(input())
      numero_turno = int(3)
      print (f"Turno: {numero_turno}")

      if ((acao_3 == "Ataque Físico") or (acao_3 == "Agi" and (resistencia_entidade != "fogo" and fraqueza_entidade != "fogo")) or (acao_3 == "Bufu" and (resistencia_entidade != "gelo" and fraqueza_entidade != "gelo")) or (acao_3 == "Zio" and (resistencia_entidade != "eletricidade" and fraqueza_entidade != "eletricidade"))):
        acao3 = True

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
          
      if(acao3 == False):

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

      if (resistencia_3 == False):    

        if (((acao_3 == "Agi" and fraqueza_entidade == "fogo" ) or (acao_3 == "Bufu" and fraqueza_entidade == "gelo") or (acao_3 == "Zio" and fraqueza_entidade == "eletricidade"))):
          meu_critico_3 = True

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