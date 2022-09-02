nome = str(input("Qual é seu nome? "))

numb = int(input ("Digite um número que respeite o intervalo 0 à 100: "))

while (numb < 0 or numb > 100):
    print (f"Esse número não é valido, {nome}!")
    numb = int(input ("Digite um número que respeite o intervalo 0 à 100: "))
else: 

    if (numb%2 == 0):
        numb += int(1)
        
    while (numb < 99):
        print (f"{numb}, " ,end = "")
        numb += int(2)


    else:
        print (f"{numb}.")