#laço de repetição fazendo a estrutura de fibonacci
Case_1_N = False
Case_2_N = False
primo = True
N = int(input())

if (N <= int(0)):
    Case_1_N = True

elif ((N > int(0)) and (N < int(3))):
    Case_2_N = True

else:
           
    star2_x = int(input())
    star2_y = int(input())
    soma_dis = int(0)
    D_aux = int(0)
    verificador = int(0)

    for i in range (1,(N)):

        star1_x = int(star2_x)
        star1_y = int(star2_y)
        star2_x = int(input())
        star2_y = int(input())
        
        D = int(((((star1_x - star2_x)**2) + ((star1_y - star2_y)**2)))**0.5)

        print (f"Distância [star{i} <-> star{(i+1)}]: {D}")
        soma_dis += int(D)
        fc = int(1)
        fc_anter = int(0)
        verifi_fibonacci = False
        for f in range (1,(D+1)):
            fcc = (fc)
            fc += int(fc_anter)
            D_aux = (D)
            fc_anter = (fcc)

            if (D == fc):
                verifi_fibonacci = True
            
        else:
            
            if (verifi_fibonacci == False):
                verificador += int(1)
    
if (Case_1_N == True):
    print ("Isso está quebrado, acho que Howard pode me ajudar.")

elif (Case_2_N == True):
    print ("Acho que bebi demais, eu juro que tinha mais estrelas!")

else: 

    for p in range (2,(soma_dis)):

        if ((soma_dis%p) == 0):
            primo = False
        
    else: 

        if (verificador == int(0)):

            if ((primo == False)):
                print ("Yes! Eu consegui!")
            
            else:
                print ("Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!")
            
        elif (verificador == int(1)):
            print ("Oh, não! Eu quase consegui!")
        
        elif (verificador >= int(2)):
            
            if ((primo == False)):
                print ("Eu vou acabar como o Stuart :/")

            else: 
                print ("Pelo menos o programa está funcionando...")