import random
import warrior
import easy
from math import floor

# Função para definir a classe
def define_Profession():
    profession_List = ['warrior']
    my_Profession = None

    while my_Profession not in profession_List: #Verifica se a classe existe
        print('---Escolha sua Profissão---')
        print('Warrior')
        print('Futuramente mais')
        my_Profession = input('Minha profissão será: ').lower()

    print(f'Sua profissão será {my_Profession}')

    # Pega os atributos básicos da classe
    if my_Profession == 'warrior':
        hp_Profession = warrior.hp
        armor_Profession = warrior.ac
    else:
        hp_Profession = 0  # Defina valores padrões para evitar erros caso outras classes sejam implementadas
        armor_Profession = 0
    
    return hp_Profession, armor_Profession, my_Profession

hp_Profession, armor_Profession, my_Profession = define_Profession()

# Definindo seus atributos
def show_Perks(perks: dict, free_Points: int) -> str:   # Mostra os atributos
    print('---Vamos definir seus atributos---')
    print(f'Você possui {free_Points} para distribuir nesses atributos')
    for perk, value in perks.items():
        print(f'{perk.capitalize()}: {value}')
    print(f'[Quit] Escolha feita (Pontos não usados serão perdidos)')

def perk_Select(perks: dict) -> str:  # Pede a escolha de um atributo
    perk_Select = None
    while perk_Select not in perks and perk_Select != 'quit':
        perk_Select = input('Digite o nome do atributo escolhido: ').lower()
        if perk_Select not in perks and perk_Select != 'quit':
            print('Opção incorreta')
    return perk_Select

def add_or_Remove() -> str:   # Pede a escolha da adição ou remoção de pontos em um atributo 
    remove_Add = None
    while remove_Add not in ['remove', 'add']:
        remove_Add = input('Você quer remove ou add pontos? ').lower()
        if remove_Add not in ['remove','add']:
            print('Opção incorreta')
    return remove_Add

def add_Points(perks, perk_Selected, free_Points):
    while True:
        try:
            # Tenta converter a entrada do usuário em um número inteiro
            points_Quantity = int(input(f'Quantos pontos de {free_Points} você quer adicionar em {perk_Selected.capitalize()}? '))

            # Verifica se a quantidade é positiva
            if points_Quantity < 0:
                print('Por favor, insira um número positivo.')
            # Verifica se o valor final ultrapassaria 20
            elif perks[perk_Selected] + points_Quantity > 20:
                print(f'Não é possível adicionar essa quantidade. {perk_Selected.capitalize()} não pode ultrapassar 20.')
            # Verifica se há pontos livres suficientes
            elif free_Points - points_Quantity >= 0:
                perks[perk_Selected] += points_Quantity
                free_Points -= points_Quantity
                break  # Sai do loop após uma entrada válida
            else:
                print('Pontos livres insuficientes')
        except ValueError:
            # Captura erros de conversão para int e pede nova entrada
            print('Por favor, insira um número inteiro válido.')   
    return free_Points


def remove_Points(perks: dict, perk_Select: str, free_Points: int) -> int:
    while True:
        try:
            # Tenta converter a entrada do usuário em um número inteiro
            points_Quantity = int(input(f'Quantos pontos você quer remover em {perk_Select.capitalize()}? '))

            # Verifica se a quantidade é positiva
            if points_Quantity < 0:
                print('Por favor, insira um número positivo.')
            # Verifica se o valor final seria menor do que 0
            elif perks[perk_Select] - points_Quantity < 0:
                print(f'Não é possível remover essa quantidade. {perk_Select.capitalize()} não pode ser menor que 0.')
            else:
                perks[perk_Select] -= points_Quantity
                free_Points += points_Quantity
                break  # Sai do loop após uma entrada válida
        except ValueError:
            # Captura erros de conversão para int e pede nova entrada
            print('Por favor, insira um número inteiro válido.')   
    return free_Points


def main_atr() -> dict: # Função principal dos atributos
    free_Points = 14
    perks = {'strength': 10, 'speed': 10, 'body': 10, 'magic': 10,}
    perk_Selected = None

    while perk_Selected != 'quit':
        show_Perks(perks, free_Points)
        perk_Selected = perk_Select(perks)
        
        if perk_Selected != 'quit':
            action_Add_Remove = add_or_Remove()
            
            if action_Add_Remove == 'add':
                free_Points = add_Points(perks, perk_Selected, free_Points)
            elif action_Add_Remove == 'remove':
                free_Points = remove_Points(perks, perk_Selected, free_Points)
    
    print("Distribuição de pontos finalizada!")
    print(f"Atributos finais: {perks}")
    return perks

perks = main_atr()

# Escolhea a arma
def weapon_Select(profession: str):
    if profession == 'warrior':
        weapons = warrior.weapons
    else:
        weapons = {}

    weapon_Select = None
    while weapon_Select not in weapons:
        print('---Escolha sua arma---')
        for weapon, weapons_Infos in weapons.items():
            print(f"{weapon} | {weapons_Infos[0]} {weapons_Infos[1]}d{weapons_Infos[2]}")
        weapon_Select = input('Insira o nome da sua arma: ').lower()

    return weapons[weapon_Select]

weapon = weapon_Select(my_Profession)
print(weapon)

# Comece o combate

action_List = ['attack',]

def select_Easy() -> list:    # Escolhe um inimigo da lista 
    enemy = easy.random_Enemy()
    return enemy

def initiative_Roll(speed: int) -> int:   # Rola a iniciativa do player
    speed_Ready = floor((speed - 10) / 2)
    roll = random.randint(1, 20)
    initiative = speed_Ready + roll
    return initiative

def enemy_Initiative_Roll(speed_enemy: int) -> int:   # Rola a iniciativa do inimigo
    roll = random.randint(1, 20)
    initiative = roll + speed_enemy
    return initiative

def who_First_Action(player_Initiative: int, enemy_Initiative: int) -> str:   # Define quem vai tomar a ação primeiro
    if player_Initiative >= enemy_Initiative:
        who_First_Action = 'player'
    else:
        who_First_Action = 'enemy'
    return who_First_Action

def hp_Ready(hp_Profession: int, body_Player: int) -> int:   # Calcula a vida do player com base na classe dele
    body_Ready = floor((body_Player - 10) / 2)
    hp_Player = body_Ready + hp_Profession
    return hp_Player

def player_Attack(strength_Player: int, armor_Enemy: int, attack_Quantity: int, damage_Weapon: int) -> int:   # Calcula a ação ataque e o dano realizado
    strength_Ready = floor((strength_Player - 10) / 2)
    attack = random.randint(1, 20) + strength_Ready
    print(f'A rolagem de ataque foi {attack}')
    if attack >= armor_Enemy:
        total_Damage = 0
        for n in range(attack_Quantity):
            damage_Roll = random.randint(1, damage_Weapon) + strength_Ready
            total_Damage += damage_Roll
        print(f'O dano total foi: {total_Damage}')    
        return total_Damage
    else:
        print('O ataque errou')
        return 0

def enemy_Attack(strength_Enemy: int, armor_Enemy: int, attack_Quantity: int, damage_Weapon: int) -> int: # Calcula a ação ataque do inimigo e o dano realizado
    attack = random.randint(1, 20) + strength_Enemy
    print(f'A rolagem de ataque foi {attack}')
    if attack >= armor_Enemy:
        total_Damage = 0
        for n in range(attack_Quantity):
            damage_Roll = random.randint(1, damage_Weapon) + strength_Enemy
            total_Damage += damage_Roll
        print(f'O dano total foi: {total_Damage}')    
        return total_Damage
    else:
        print('O ataque errou')
        return 0
    
def easy_Fight(): # Função principal do combate no fácil
    enemy = select_Easy()
    hp_Enemy = enemy[1]
    hp_Player = hp_Ready(hp_Profession, perks['body'])
    print(f'Seu inimigo é {enemy[0]}')
    print('Vamos rolar as iniciativas')
    initiative_Player = initiative_Roll(perks['speed'])
    print(f'Sua iniciativa foi: {initiative_Player}')
    initiative_Enemy = enemy_Initiative_Roll(enemy[4][1])
    print(f'A iniciativa do {enemy[0]} foi: {initiative_Enemy}')
    first_Action = who_First_Action(initiative_Player, initiative_Enemy)
    while hp_Enemy > 0 and hp_Player > 0: # Verifica se alguém tem a vida menor do que 0
        if first_Action == 'player':   # Player começa
            action_Select = None    # Turno do player
            while action_Select not in action_List: 
                print('---Seu turno!---')
                print('Attack')
                action_Select = input('Escolha sua ação: ').lower()
            if action_Select == 'attack':
                total_Damage = player_Attack(perks['strength'], enemy[2], weapon[1], weapon[2])
                hp_Enemy -= total_Damage
                print(f'A vida do seu inimigo é {hp_Enemy}')
            if hp_Enemy <= 0: # Verifica se o inimigo morreu
                break
            print(f'---Turno do {enemy[0]}---')   # Turno do inimigo
            total_Damage = enemy_Attack(enemy[3][2], armor_Profession, enemy[3][0], enemy[3][1])
            hp_Player -= total_Damage
            print(f'A sua vida é {hp_Player}')
        else:
            print(f'---Turno do {enemy[0]}---')   # Turno do inimigo
            total_Damage = enemy_Attack(enemy[3][2], armor_Profession, enemy[3][0], enemy[3][1])
            hp_Player -= total_Damage
            print(f'A sua vida é {hp_Player}')
            if hp_Player <= 0:    # Verifica a vida do player
                break
            action_Select = None    # Turno do player
            while action_Select not in action_List: 
                print('---Seu turno---')
                print('Attack')
                action_Select = input('Escolha sua ação: ').lower()
            if action_Select == 'attack':
                total_Damage = player_Attack(perks['strength'], enemy[2], weapon[1], weapon[2])
                hp_Enemy -= total_Damage
            print(f'A vida do seu inimigo é {hp_Enemy}')

    if hp_Enemy <= 0:
        print(f'O {enemy[0]} morreu')
        print(f'Você sobreviveu com {hp_Player} de HP')
        live_Death = 'vivo'
        return live_Death
    else:
        print(f'Você morreu')
        live_Death = 'morto'
        return live_Death
    

# Escolha de dificuldade
difficulty_List = ['easy']

while True:
    live_Death = 'Vivo'
    difficulty_Select = None
    while difficulty_Select not in difficulty_List:
        print('---Escolha a dificuldade dos encontros---')
        print('Easy')
        difficulty_Select = input('Dificuldade: ').lower()
    if difficulty_Select == 'easy':
        easy_Fight()
