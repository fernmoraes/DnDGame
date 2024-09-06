import random
import warrior
import easy
from math import floor

# Função para definir a classe
def definir_classe():
    op_classes = ['warrior']
    escolha_classe = None

    while escolha_classe not in op_classes: #Verifica se a classe existe
        print('---Escolha sua Classe---')
        print('Warrior')
        print('Futuramente mais')
        escolha_classe = input('Minha classe será: ').lower()

    print(f'Sua classe será {escolha_classe}')
    
    # Pega os atributos básicos da classe
    if escolha_classe == 'warrior':
        vida_classe = warrior.hp
        armadura_classe = warrior.ac
    else:
        vida_classe = 0  # Defina valores padrões para evitar erros caso outras classes sejam implementadas
        armadura_classe = 0
    
    return vida_classe, armadura_classe, escolha_classe

vida_classe, armadura_classe, escolha_classe = definir_classe()

# Definindo seus atributos
def exibir_atributos(atributos: dict, pontos_livres: int) -> str:   # Mostra os atributos
    print('---Vamos definir seus atributos---')
    print(f'Você possui {pontos_livres} para distribuir nesses atributos')
    for atributo, valor in atributos.items():
        print(f'{atributo.capitalize()}: {valor}')
    print(f'[Quit] Escolha feita (Pontos não usados serão perdidos)')

def escolher_atributo(atributos: dict) -> str:  # Pede a escolha de um atributo
    escolha_atributos = None
    while escolha_atributos not in atributos and escolha_atributos != 'quit':
        escolha_atributos = input('Digite o nome do atributo escolhido: ').lower()
        if escolha_atributos not in atributos and escolha_atributos != 'quit':
            print('Opção incorreta')
    return escolha_atributos

def escolher_add_remove() -> str:   # Pede a escolha da adição ou remoção de pontos em um atributo 
    remover_adicionar = None
    while remover_adicionar not in ['remove', 'add']:
        remover_adicionar = input('Você quer remove ou add pontos? ').lower()
        if remover_adicionar not in ['remove','add']:
            print('Opção incorreta')
    return remover_adicionar

def adicionar_pontos(atributos, escolha_atributos, pontos_livres):
    while True:
        try:
            # Tenta converter a entrada do usuário em um número inteiro
            quantidade_atributo = int(input(f'Quantos pontos de {pontos_livres} você quer adicionar em {escolha_atributos.capitalize()}? '))

            # Verifica se a quantidade é positiva
            if quantidade_atributo < 0:
                print('Por favor, insira um número positivo.')
            # Verifica se o valor final ultrapassaria 20
            elif atributos[escolha_atributos] + quantidade_atributo > 20:
                print(f'Não é possível adicionar essa quantidade. {escolha_atributos.capitalize()} não pode ultrapassar 20.')
            # Verifica se há pontos livres suficientes
            elif pontos_livres - quantidade_atributo >= 0:
                atributos[escolha_atributos] += quantidade_atributo
                pontos_livres -= quantidade_atributo
                break  # Sai do loop após uma entrada válida
            else:
                print('Pontos livres insuficientes')
        except ValueError:
            # Captura erros de conversão para int e pede nova entrada
            print('Por favor, insira um número inteiro válido.')   
    return pontos_livres


def remover_pontos(atributos: dict, escolha_atributos: str, pontos_livres: int) -> int:
    while True:
        try:
            # Tenta converter a entrada do usuário em um número inteiro
            quantidade_atributo = int(input(f'Quantos pontos você quer remover em {escolha_atributos.capitalize()}? '))

            # Verifica se a quantidade é positiva
            if quantidade_atributo < 0:
                print('Por favor, insira um número positivo.')
            # Verifica se o valor final seria menor do que 0
            elif atributos[escolha_atributos] - quantidade_atributo < 0:
                print(f'Não é possível remover essa quantidade. {escolha_atributos.capitalize()} não pode ser menor que 0.')
            else:
                atributos[escolha_atributos] -= quantidade_atributo
                pontos_livres += quantidade_atributo
                break  # Sai do loop após uma entrada válida
        except ValueError:
            # Captura erros de conversão para int e pede nova entrada
            print('Por favor, insira um número inteiro válido.')   
    return pontos_livres


def main_atr() -> dict: # Função principal dos atributos
    pontos_livres = 14
    atributos = {'strength': 10, 'speed': 10, 'body': 10, 'magic': 10,}
    escolha_atributos = None

    while escolha_atributos != 'quit':
        exibir_atributos(atributos, pontos_livres)
        escolha_atributos = escolher_atributo(atributos)
        
        if escolha_atributos != 'quit':
            acao = escolher_add_remove()
            
            if acao == 'add':
                pontos_livres = adicionar_pontos(atributos, escolha_atributos, pontos_livres)
            elif acao == 'remove':
                pontos_livres = remover_pontos(atributos, escolha_atributos, pontos_livres)
    
    print("Distribuição de pontos finalizada!")
    print(f"Atributos finais: {atributos}")
    return atributos

atributos = main_atr()

# Escolhea a arma
def escolher_arma(classe: str):
    if classe == 'warrior':
        armas = warrior.weapons
    else:
        armas = {}

    escolha_arma = None
    while escolha_arma not in armas:
        print('---Escolha sua arma---')
        for arma, detalhes in armas.items():
            print(f"{arma} | {detalhes[0]} {detalhes[1]}d{detalhes[2]}")
        escolha_arma = input('Insira o nome da sua arma: ').lower()

    return armas[escolha_arma]

arma = escolher_arma(escolha_classe)
print(arma)

# Comece o combate

opcoes_acao = ['attack',]

def escolher_easy() -> list:    # Escolhe um inimigo da lista 
    inimigo = easy.randomizar_inimigo()
    return inimigo

def rolagem_iniciativa(speed: int) -> int:   # Rola a iniciativa do player
    speed_calculada = floor((speed - 10) / 2)
    rolagem = random.randint(1, 20)
    iniciativa = speed_calculada + rolagem
    return iniciativa

def rolagem_iniciativa_inimigo(speed_enemy: int) -> int:   # Rola a iniciativa do inimigo
    rolagem = random.randint(1, 20)
    iniciativa = rolagem + speed_enemy
    return iniciativa

def primeiro(iniciativa_player: int, iniciativa_inimigo: int) -> str:   # Define quem vai tomar a ação primeiro
    if iniciativa_player >= iniciativa_inimigo:
        primeira_acao = 'player'
    else:
        primeira_acao = 'enemy'
    return primeira_acao

def calcular_vida(vida_classe: int, body_player: int) -> int:   # Calcula a vida do player com base na classe dele
    body_calculada = floor((body_player - 10) / 2)
    hp_player = body_calculada + vida_classe
    return hp_player

def player_atacar(strength_player: int, ac_inimigo: int, dado: int, dano: int) -> int:   # Calcula a ação ataque e o dano realizado
    strength_calculada = floor((strength_player - 10) / 2)
    ataque = random.randint(1, 20) + strength_calculada
    print(f'A rolagem de ataque foi {ataque}')
    if ataque >= ac_inimigo:
        dano_total = 0
        for n in range(dado):
            dano_rolado = random.randint(1, dano) + strength_calculada
            dano_total += dano_rolado
        print(f'O dano total foi: {dano_total}')    
        return dano_total
    else:
        print('O ataque errou')
        return 0

def inimigo_atacar(strength_enemy: int, ac_player: int, dado: int, dano: int) -> int: # Calcula a ação ataque do inimigo e o dano realizado
    ataque = random.randint(1, 20) + strength_enemy
    print(f'A rolagem de ataque foi {ataque}')
    if ataque >= ac_player:
        dano_total = 0
        for n in range(dado):
            dano_rolado = random.randint(1, dano) + strength_enemy
            dano_total += dano_rolado
        print(f'O dano total foi: {dano_total}')    
        return dano_total
    else:
        print('O ataque errou')
        return 0
    
def combate_easy(): # Função principal do combate no fácil
    enemy = escolher_easy()
    hp_enemy = enemy[1]
    hp_player = calcular_vida(vida_classe, atributos['body'])
    print(f'Seu inimigo é {enemy[0]}')
    print('Vamos rolar as iniciativas')
    iniciativa_player = rolagem_iniciativa(atributos['speed'])
    print(f'Sua iniciativa foi: {iniciativa_player}')
    iniciativa_inimigo = rolagem_iniciativa_inimigo(enemy[4][1])
    print(f'A iniciativa do {enemy[0]} foi: {iniciativa_inimigo}')
    primeira_acao = primeiro(iniciativa_player, iniciativa_inimigo)
    while hp_enemy > 0 and hp_player > 0: # Verifica se alguém tem a vida menor do que 0
        if primeira_acao == 'player':   # Player começa
            escolher_acao = None    # Turno do player
            while escolher_acao not in opcoes_acao: 
                print('---Seu turno!---')
                print('Attack')
                escolher_acao = input('Escolha sua ação: ').lower()
            if escolher_acao == 'attack':
                dano_total = player_atacar(atributos['strength'], enemy[2], arma[1], arma[2])
                hp_enemy -= dano_total
                print(f'A vida do seu inimigo é {hp_enemy}')
            if hp_enemy <= 0: # Verifica se o inimigo morreu
                break
            print(f'---Turno do {enemy[0]}---')   # Turno do inimigo
            dano_total = inimigo_atacar(enemy[3][2], armadura_classe, enemy[3][0], enemy[3][1])
            hp_player -= dano_total
            print(f'A sua vida é {hp_player}')
        else:
            print(f'---Turno do {enemy[0]}---')   # Turno do inimigo
            dano_total = inimigo_atacar(enemy[3][2], armadura_classe, enemy[3][0], enemy[3][1])
            hp_player -= dano_total
            print(f'A sua vida é {hp_player}')
            if hp_player <= 0:    # Verifica a vida do player
                break
            escolher_acao = None    # Turno do player
            while escolher_acao not in opcoes_acao: 
                print('---Seu turno---')
                print('Attack')
                escolher_acao = input('3112Escolha sua ação: ').lower()
            if escolher_acao == 'attack':
                dano_total = player_atacar(atributos['strength'], enemy[2], arma[1], arma[2])
                hp_enemy -= dano_total
            print(f'A vida do seu inimigo é {hp_enemy}')

    if hp_enemy <= 0:
        print(f'O {enemy[0]} morreu')
        print(f'Você sobreviveu com {hp_player} de HP')
        estado = 'vivo'
        return estado
    else:
        print(f'Você morreu')
        estado = 'morto'
        return estado
    

# Escolha de dificuldade
opcoes_dificuldade = ['easy']

while True:
    estado = 'Vivo'
    escolha_dificuldade = None
    while escolha_dificuldade not in opcoes_dificuldade:
        print('---Escolha a dificuldade dos encontros---')
        print('Easy')
        escolha_dificuldade = input('Dificuldade: ').lower()
    if escolha_dificuldade == 'Easy':
        combate_easy()
