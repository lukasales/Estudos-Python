from unicodedata import numeric


print("vamos desobrir o seu índice de massa corporal? \nPara isso precisamos de apenas duas informações, certo?")

peso = float(input("Digite o valor do seu peso: "))
altura = float(input("Digite o valor da sua altura: "))

IMC = float(peso/(altura**2))

if (IMC <= 18.5):
    print(f"O seu IMC é {IMC} e você está abaixo do peso!")

elif (IMC <= 25):
    print(f"O seu IMC é {IMC} e você está no peso normal!")

elif (IMC <= 30):
    print(f"O seu IMC é {IMC} e você está acima do peso!")

elif (IMC > 30):
    print(f"O seu IMC é {IMC} e você está obeso, cuidado!")