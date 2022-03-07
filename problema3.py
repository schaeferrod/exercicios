#Objetivo do programa:
#
area_pintura = float(input("Qual o tamanho da área a ser pintada? (m2)\n"))

medida_da_lata = float(18)
custo_da_lata = int(80)

qtd_em_litro = area_pintura/3

qtd_de_lata = qtd_em_litro/medida_da_lata

if qtd_de_lata >= 0:
    qtd_de_lata = int(qtd_de_lata +1)


preço_total = qtd_de_lata*custo_da_lata

print(f"Quantidade de latas: {qtd_de_lata}")
print(f"Preço total: {preço_total}")
