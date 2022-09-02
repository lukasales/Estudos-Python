nome = str(input("Qual é o seu nome? "))
numb = int(0)
square = int((numb)**2)
cube = int((numb)**3)

print (f"{nome}! Bem vindo a um pequeno teste \n \n")
print ("Number    Square    Cube\n")

while (numb <= 10):
    print (f"{numb}         {square}         {cube}\n")
    numb += int(1)
    square = int((numb)**2)
    cube = int((numb)**3)

else:
    print ("Fim do programa.")
