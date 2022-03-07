#teste de uma solução que vi do github para o problema 3
tamanho = float(input('Entre com o tamanho da área: '))

litros = tamanho / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1
preco = latas * 80

print(latas)
