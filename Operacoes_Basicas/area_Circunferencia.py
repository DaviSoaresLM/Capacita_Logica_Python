# Faça um programa para ler um valor real R representando o raio da circunferência que Bino que calcular a área. Imprima a área da circunferência utilizando como pi o valor 3.1416.
R = float(input("Digite o valor do raio da circunferência: "))
PI = 3.1416

AREA = PI * (R**2)

print(f"A área da circunferência é: {AREA:.2f}")
