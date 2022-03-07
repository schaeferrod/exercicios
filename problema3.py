#Rodrigo Schaefer da Silva
#Objetivo do programa:
#Pedir o tamanho em metros quadrados da área
#Considerar que 1 litro de tinta é suficiente para pintar 3 m2
#Tinta é vendida em latas de 18l por R$80
#Informar ao user a qtd de latas de tinta e o preço
area_pintura = float(input("Qual o tamanho da área a ser pintada? (m2)\n"))

medida_da_lata = float(18)
custo_da_lata = int(80)

qtd_em_litro = area_pintura/3

qtd_de_lata = qtd_em_litro/medida_da_lata

if (qtd_em_litro%18) != 0: #Essa condição resolve o problema para ele não considerar múltiplos de 18 ao somar 1 na qtd de lata para o arredondamento
    qtd_de_lata = int(qtd_de_lata +1)


preço_total = qtd_de_lata*custo_da_lata

print(f"Quantidade de latas: {qtd_de_lata}")
print(f"Preço total: {preço_total}")
