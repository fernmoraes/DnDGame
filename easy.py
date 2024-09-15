import random

# [Nome, vida, armadura,[dado, dano, bonus], [strength, speed, body, magic]] 
enemy_Easy_List = [['Goblin', 7, 15, [1, 6, 2], [-1, 2, 0, 0,]], 
              ['Kobold', 5, 12, [1, 4, 2], [-2, 2, -1, -1,]], 
              ['Esqueleto', 13, 13, [1, 6, 2], [0, 2, 2, -2,]],
              ['Orcs', 15, 13, [1, 12, 3], [3, 1, 3, -2,]], 
              ['Lobos', 11, 13, [2, 4, 2], [1, 2, 1, -4,]], 
              ['Zumbis', 22, 8, [1, 6, 1], [1, -2, 3, -4,]], 
              ['Aranha Gigantes', 26, 14, [2, 8, 3], [2, 3, 1, -4,]]]

# [Nome, tipo, quantidade, [dado, quantidade de cura]]
easy_Loot_List = [['Cura Pequena', 'cura', 1, [1, 8]],
                  ['Cura Media', 'cura', 2, [1, 8]]]

def random_Enemy() -> list:
    enemy_Selected = random.randint(0, 6)
    enemy = enemy_Easy_List[enemy_Selected]
    return enemy