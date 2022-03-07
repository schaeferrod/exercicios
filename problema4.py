int1 = int(input("Qual a primeiro valor inteiro?\n"))
int2 = int(input("Qual a segundo valor inteiro?\n"))
float1 = float(input("Qual o valor float?\n"))

calculo1 = (2*int1)*(int2/2)
calculo2 = (3*int1)+float1
calculo3 = float1**3

print("1 - O produto do dobro do primeiro com metade do segundo.")
print("2 - A soma do triplo do primeiro com o terceiro.")
print("3 - O terceiro elevado ao cubo.")

print(f"Os valores são os seguintes:\n1 - {calculo1}\n2 - {calculo2}\n3 - {calculo3}")
