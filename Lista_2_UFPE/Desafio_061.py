batida = str(input())

while (batida != str("Boa noite")):
    check = int(0)

    for i in range (1, 4):
        
        if (batida == str("toc-toc-toc")):
            batida = str(input())

            if (batida == str("Penny")):
                check += int(1)
                print (check)

                if (check == int(3)):
                    check = int(0)
                    print ("Pode entrar Sheldon")
                    batida = str(input())

                else:
                    batida = str(input())

            else:
                print ("Não pode entrar, se identifique!!!")
                check = int(0)
                batida = str(input())    
        
        else:
            print (check)
            print ("Não pode entrar, se identifique!!!")
            check = int(0)
            batida = str(input())
            break

else: 
    print ("Boa noite Penny")
