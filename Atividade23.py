# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
num = int(input("Digite se número para mostrar seus multiplicadores de 1 a 10: "))

for ta in range (11):
    print(f"{num} * {ta} = {ta*num}")

