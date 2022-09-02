print ("Aprendendo a usar a tag 'range'.")

numb = int(input("Escreva um número entre 0 e 100: "))

while ((numb < 0) or (numb > 100)):
    print ("Número invalido, tente novamente!")
    numb = int(input("Escreva um número entre 0 e 100: "))

if (numb%2 == 0):
    numb += int(1)


for i in range (numb,98, 2):
    print (f"{i}, " ,end="")
    numb += int(2)

else: 
    print (f"{numb}.")