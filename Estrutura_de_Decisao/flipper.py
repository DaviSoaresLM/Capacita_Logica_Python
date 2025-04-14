"""
Flíper é um tipo de jogo onde uma bolinha de metal cai por um labirinto de caminhos até chegar à parte de baixo. A quantidade de pontos que o jogador ganha depende do caminho que a bolinha seguir.

O jogador pode controlar o percurso da bolinha mudando a posição de algumas portinhas do labirinto. Cada portinha pode estar na posição 0, que significa virada para a esquerda, ou na posição 1, que significa virada para a direita.

Considere o flíper da figura abaixo, que tem duas portinhas. A portinha P está na posição 1, e a portinha R está na posição 0.
"""

print("----- Flíper-----")
p = int(input("Digite '0' para Esquerda e '1' para Direita: "))
r = int(input("Digite '0' p/ Esquerda e '1' p/ Direita: "))

if p == 1:
    print("A bola caiu no caminho C")
elif p == 0:
    if r == 0:
        print("A bola caiu no caminho A")
    else:
        print("A bola caiu no caminho B")
else:
    print("Valor não compatível, digite 0 ou 1 para escolher o caminho")
