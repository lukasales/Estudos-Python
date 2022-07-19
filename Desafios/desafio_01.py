nota = float(input("Qual foi sua nota? "))

if (nota < float(3.0)):
    print ("E")
elif (nota < float(5.0)):
    print ("D")
elif (nota < float(7.0)):
    print ("C")
elif nota < float(8.5):
    print ("B")
elif nota < float(10.0):
    print ("A")
else: 
    print ("Essa nota não é permitida nos intervalos de 0 a 10!")