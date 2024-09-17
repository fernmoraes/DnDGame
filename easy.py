import random
import copy  # Para copiar profundamente o dicionário

# Definição dos inimigos
enemies_Easy = {'Goblin': {'name': 'Goblin', 'hp': 7, 'armor': 15, 'weapon': [1, 6], 'stats': [8, 14, 10, 10]},
                'Kobold': {'name': 'Kobold', 'hp': 5, 'armor': 12, 'weapon': [1, 4], 'stats': [6, 14, 8, 8]},
                'Esqueleto': {'name': 'Esqueleto', 'hp': 13, 'armor': 13, 'weapon': [1, 6], 'stats': [10, 14, 14, 6]},
                'Zumbi': {'name': 'Zumbi', 'hp': 22, 'armor': 8, 'weapon': [1, 6], 'stats': [12, 6, 16, 2]}}

# Definição dos loots
easy_Loots = [['Cura Pequena', 'cura', [1, 8]],
              ['Cura Media', 'cura', [1, 8]]]

# Função para escolher inimigo aleatório com cópia profunda
def random_Enemy() -> dict:
    enemy_name = random.choice(list(enemies_Easy.keys()))
    chosen_enemy = copy.deepcopy(enemies_Easy[enemy_name])  # Copiar profundamente o inimigo
    return chosen_enemy