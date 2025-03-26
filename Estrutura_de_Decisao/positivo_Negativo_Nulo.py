"""Faça um programa para ler um inteiro x. Imprima a mensagem "positivo" se o valor for positivo.
Imprima a mensagem "negativo" caso o valor seja negativo. Imprima a mensagem "nulo" se o valor for zero.
"""

x = int(input("Digite um número intero: "))

if x == 0:
    print("Nulo")
elif x > 0:
    print("Positivo")
else:
    print("Negativo")
