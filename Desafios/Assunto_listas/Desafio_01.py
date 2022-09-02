from itertools import count


produtos_vendidos = ["martelo", "alicate", "chave de fenda", "chave estrela", "tesoura"]

produtos_estoque = ["martelo", "alicate", "martelo", "martelo", "chave de fenda", "alicate", "chave estrela"]

consulta = str(input("Qual produto deseja adquirir? "))

#verificar se a loja vende o produto 
cons = False
for vend_produto in (produtos_vendidos):

    if ( vend_produto == consulta):
        cons = True

#verificar no estoque
if (cons):
    quantidade = int(0)
    for estoq_produtos in produtos_estoque:
        if (estoq_produtos == consulta):
            quantidade += int(1)
    
if (cons == True):

    if (quantidade > 0):
        print(f"Temos {quantidade} {consulta} em estoque!")
        resp = str(input("Deseja adquirir algum? "))

        while (resp != "sim" and resp != "não"):
            print ("Senhor preciso de uma resposta para concluir o atendimento")
            resp = str(input("Deseja adquirir quantos? "))

        else:

            if (resp == "não"):
                print ("Tudo bem, tenha um bom dia!")
            
            else:
                quanti_produt_vendidos = int(input("Otimo! Quantos o senhor deseja levar? "))
                produt_estoque_atualizado = produtos_estoque.count(consulta)
                estoque_dps_venda = int(produt_estoque_atualizado - quanti_produt_vendidos)
                produtos_estoque.remove(consulta)
                print (f"Agora temos o total de {estoque_dps_venda} no estoque!")

    else: 
        print (f"Vendemos o {consulta}, porém, atualmente, não temos ele em estoque")
else:
    print("Esse produto não é vendido na nossa loja")