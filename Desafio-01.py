#mensagem inicial
nome = str(input("Qual é o seu nome? "))
print ('Seja Bem Vindo, '+ nome + '!')

#bloco do gasto calórico
taxa_metabolica_basal = int(input('Qual o valor da sua taxa metabolica basal durante o dia de hoje? '))
media_calorias_gastas = int(input('Qual é a média das suas calorias gastas praticando atividades físicas? '))
quantidade_exercicios = int(input('Quantas vezes por semana você faz atividades físicas? '))
descanso_durante_ano = int(input('Quantos mêses por ano você descansa? '))
total_exercicios = (quantidade_exercicios * 4)
total_exercicios_ano = ((12-descanso_durante_ano)*total_exercicios)
total_calorias_gastas = (total_exercicios_ano * media_calorias_gastas)
total_tmb_ano = (taxa_metabolica_basal * 7 * 4 * 12)
resultado_calorico_gasto = (total_calorias_gastas + total_tmb_ano)

#impressão do relátorio do gasto calórico
print (nome, 'Você gasta ao ano um total de ' ,str(resultado_calorico_gasto))

#bloco do consumo calórico anual
consumo_medio_calorias_refei = int(input('Qual a média do seu consumo de calorias por refeição? '))
numero_refei_dia = int(input('Quantas refeições você faz ao dias? '))
total_consu_calorico = (numero_refei_dia * 7 * 4 * 12 * consumo_medio_calorias_refei)

#impressão do relátorio de consumo calórico
print (nome, '! Você consome um total de' ,total_consu_calorico, 'calorias por ano')

#bloco de condições 
if (total_consu_calorico > resultado_calorico_gasto): 
    print ('Você está consumindo mais do que gasta! precisa gastar mais que', str(total_consu_calorico - resultado_calorico_gasto))
elif (total_consu_calorico == resultado_calorico_gasto):
    print ('Você não esta ganhando nem perdendo peso!')
elif (total_consu_calorico < resultado_calorico_gasto):
    print ('Você esta emagrecendo,',nome, ', Parabéns!')