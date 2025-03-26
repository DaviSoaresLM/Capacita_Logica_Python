# Faça um programa que leia dois números reais A e B digitados pelo teclado e imprima a divisão de A por B
A = float(input("Digite o número real: "))
B = float(input("Digite o segundo número real: "))

if B != 0:
    resultado = A / B
    print(f"{resultado:.2f}")
else:
    print("Erro de divisão por zero")
