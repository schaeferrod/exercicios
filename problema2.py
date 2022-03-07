#Faça um programa que pergunte o nome e a idade do user e o exiba na tela
nome = input("Oi, qual seu nome?\n")
idade = float((input("Qual sua idade?\n")))
#print("Bem vindo %s,fico feliz em saber que tens %f anos" %( nome,idade))
print(f"Bem vindo {nome}, fico feliz em saber que tens {idade} anos")
