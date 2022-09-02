nome = str(input("Qual é o seu nome? "))

print (f"{nome}! Vamos fazer um teste! \n \n")

print ("Number    Square    Cube\n")

for i in range (0, 11, 1):
    number = int(i)
    square = int((i)**2)
    cube = int((i)**3)
    print (f"{number}         {square}         {cube}\n")

else: 
    print ("Fim do programa")