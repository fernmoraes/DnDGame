import random
import warrior
import easy
import character
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
        hp_Profession = warrior.hp_Profession
        armor_Profession = warrior.armor_Profession
    else:
        hp_Profession = 0  # Defina valores padrões para evitar erros caso outras classes sejam implementadas
        armor_Profession = 0
    
    return hp_Profession, armor_Profession, my_Profession

character.hp, character.armor, character.profession = define_Profession()

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


def main_atr(perks: dict, free_Points: int) -> dict: # Função principal dos atributos
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
    return perks, free_Points

character.stats, character.free_Points = main_atr(character.stats, character.free_Points)

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

character.player_Weapon = weapon_Select(character.profession)
print(character.player_Weapon)

# Comece o combate

def hp_Ready(hp_Profession: int, body_Player: int) -> int:   # Calcula a vida do player com base na classe dele
    body_Ready = floor((body_Player - 10) / 2)
    hp_Player = body_Ready + hp_Profession
    return hp_Player

def running(speed_Runner: int, speed_Enemy: int) -> str:
    speed_Runner_Ready = floor((speed_Runner - 10) / 2)
    speed_Enemy_Ready = floor((speed_Enemy - 10) / 2)
    roll_Runner = random.randint(1, 20) + speed_Runner_Ready
    roll_Enemy = random.randint(1, 20) + speed_Enemy_Ready
    if roll_Runner > roll_Enemy:
        return 'success'
    else:
        return 'fail'

def Attack(strength_Attacker: int, armor_Enemy: int, attack_Quantity: int, damage_Weapon: int) -> int:   # Calcula a ação ataque e o dano realizado
    strength_Ready = floor((strength_Attacker - 10) / 2)
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

def check_inventory(inventory: list):
    print('---INVENTÁRIO---')
    for n in inventory:
        print(f'Item: {inventory(n)(0)}|Tipo: {inventory(n)(1)}')

def action()-> str:
    action_List = ['attack', 'inventory', 'run']
    action_Select = None
    while action_Select not in action_List: 
        print('---Seu turno!---')
        print('Attack')
        print('Inventory')
        print('Run')
        action_Select = input('Escolha sua ação: ').lower()
        return action_Select   

def fight(): # Função principal do combate no fácil
    enemy = easy.random_Enemy()
    hp_Player = hp_Ready(character.hp, character.stats['body'])
    print(f'Seu inimigo é {enemy['name']}')

    while enemy['hp'] > 0 and hp_Player > 0: # Verifica se alguém tem a vida menor do que 0
        action_Select = action()
        if action_Select == 'run':
            run = running(character.stats['speed'], enemy['stats'][2])
            if run == 'success':
                print('Você conseguiu escapar')
                live_Death = 'vivo'
                loot_Challenge = None           
                return live_Death, loot_Challenge
            else:
                print('Você não conseguiu escapar')
        if action_Select == 'inventory':
            check_inventory(character.inventory)
        if action_Select == 'attack':
            total_Damage = Attack(character.stats['strength'], enemy['armor'], character.player_Weapon[1], character.player_Weapon[2])
            enemy['hp'] -= total_Damage
            print(f'A vida do seu inimigo é {enemy['hp']}') 
        if enemy['hp'] <= 0: # Verifica se o inimigo morreu
            break
        print(f'---Turno do {enemy['name']}---')   # Turno do inimigo
        total_Damage = Attack(enemy['stats'][0], character.armor, enemy['weapon'][0], enemy['weapon'][1])
        hp_Player -= total_Damage
        print(f'A sua vida é {hp_Player}')
        if hp_Player <= 0:    # Verifica a vida do player
            break
    if enemy['hp'] <= 0:
        print(f'O {enemy['name']} morreu')
        print(f'Você sobreviveu com {hp_Player} de HP')
        live_Death = 'vivo'
        loot_Challenge = 'easy'
        return live_Death, loot_Challenge
    elif enemy['hp'] > 0:
        print(f'Você morreu')
        live_Death = 'morto'
        loot_Challenge = 'no'
        return live_Death, loot_Challenge
    else:
        live_Death = 'vivo'
        loot_Challenge = 'no'
        return live_Death, loot_Challenge
    
# Sistema de Loot
def loot_Chance()->str:
    if random.randint(1,10) >= 3:
        loot = 'yes'
    else:
        loot = 'no'
    return loot

def which_Loot(loot_Challenge: str) -> str:
    if loot_Challenge == 'easy':
        loot_Selected = random.randrange(len(easy.easy_Loots))  # randrange gera um índice de 0 até len-1
        loot = easy.easy_Loots[loot_Selected]
        return loot

# Escolha de dificuldade
difficulty_List = ['easy']
live_Death = 'vivo'

while live_Death != 'morto':
    difficulty_Select = None
    while difficulty_Select not in difficulty_List:
        print('---Escolha a dificuldade dos encontros---')
        print('Easy')
        difficulty_Select = input('Dificuldade: ').lower()
    if difficulty_Select == 'easy':
        live_Death, loot_Challenge = fight()
    if loot_Challenge != 'no':
        have_Loot = loot_Chance()
        if have_Loot == 'yes':
            loot = which_Loot(loot_Challenge)
            character.inventory.append(loot)
            print(f'Você encontrou {loot[0]}')
        if have_Loot == 'no':
            print(f'O inimigo não tinha loot :(')
