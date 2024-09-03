import random

# [Nome, vida, armadura,[dado, dano, bonus], [for, des, cons, int,sab, car]] 
lista_easy = [['Goblin', 7, 15, [1, 6, 2], [-1, 2, 0, 0, -1, -1]], 
              ['Kobold', 5, 12, [1, 4, 2], [-2, 2, -1, -1, -2, -1]], 
              ['Esqueleto', 13, 13, [1, 6, 2], [0, 2, 2, -2, -1, -3]],
              ['Orcs', 15, 13, [1, 12, 3], [3, 1, 3, -2, 0, 0]], 
              ['Lobos', 11, 13, [2, 4, 2], [1, 2, 1, -4, 1, -2]], 
              ['Zumbis', 22, 8, [1, 6, 1], [1, -2, 3, -4, -2, -3]], 
              ['Aranha Gigantes', 26, 14, [3, 8, 3], [2, 3, 1, -4, 0, -3]]]

def randomizar_inimigo() -> int:
    num_inimigo = random.randint(0, 6)
    return num_inimigo

inimigo_escolhido = lista_easy[randomizar_inimigo()]
print(inimigo_escolhido)