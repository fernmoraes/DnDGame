import random

# [Nome, vida, armadura,[dado, dano, bonus], [for, des, cons, int,sab, car]] 
enemy_Easy_List = [['Goblin', 7, 15, [1, 6, 2], [-1, 2, 0, 0, -1, -1]], 
              ['Kobold', 5, 12, [1, 4, 2], [-2, 2, -1, -1, -2, -1]], 
              ['Esqueleto', 13, 13, [1, 6, 2], [0, 2, 2, -2, -1, -3]],
              ['Orcs', 15, 13, [1, 12, 3], [3, 1, 3, -2, 0, 0]], 
              ['Lobos', 11, 13, [2, 4, 2], [1, 2, 1, -4, 1, -2]], 
              ['Zumbis', 22, 8, [1, 6, 1], [1, -2, 3, -4, -2, -3]], 
              ['Aranha Gigantes', 26, 14, [2, 8, 3], [2, 3, 1, -4, 0, -3]]]

# [Nome, tipo, quantidade, [dado, quantidade de cura]]
easy_Loot_List = [['Cura Pequena', 'cura', 1, [1, 8]],
                  ['Cura Media', 'cura', 2, [1, 8]]]

def random_Enemy() -> list:
    enemy_Selected = random.randint(0, 6)
    enemy = enemy_Easy_List[enemy_Selected]
    return enemy