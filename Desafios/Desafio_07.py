nome = str(input("Qual é seu nome? "))

print (f"{nome}! vamos treinar a tabuada de multiplicação?")

numb_aux = int(1)
numb = int(input("Digite um número aqui: "))
numb_resp = (numb)

while (numb == 0):
    print (f"{nome}! Esse número é invalido")
    numb = int(input("Digite um número aqui: "))

else:

    while ((numb_resp < (numb * 10)) or (numb_resp > (numb*(10)))):
        print(f"{numb} X {numb_aux} é igual a: {numb_resp} \n" ,end= "")
        numb_resp += int(numb)
        numb_aux += int(1)
    
    else: 
        print (f"{numb_resp}.")