batida = str(input())
check = int(0)

while (batida != str("Boa noite Penny")):
   
    for i in range (1, 4):
        batida = str(input())
        
        if (batida == str("Penny")):
            check += int(1)
            batida = str(input())
        

        if (batida != str("toc-toc-toc")):
            print (check)
            print ("Não pode entrar, se identifique!!!")
            check = int(0)
    
            if (check == int(3)):
                print ("Pode entrar Sheldon")
else:
    print ("Boa noite Penny")