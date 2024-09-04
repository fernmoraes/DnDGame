import random
import warrior
import easy
from math import floor
escolha_arma = None


# Função para definir a classe
def definir_classe():
    op_classes = ['Guerreiro']
    escolha_classe = None

    while escolha_classe not in op_classes:
        print('---Escolha sua Classe---')
        print('Guerreiro')
        print('Futuramente mais')
        escolha_classe = input('Minha classe será: ').capitalize()

    print(f'Sua classe será {escolha_classe}')
    
    if escolha_classe == 'Guerreiro':
        vida_classe = warrior.vida
        armadura_classe = warrior.armadura
    else:
        vida_classe = 0  # Defina valores padrões para evitar erros caso outras classes sejam implementadas
        armadura_classe = 0
    
    return vida_classe, armadura_classe, escolha_classe

# Exemplo de uso
vida_classe, armadura_classe, escolha_classe = definir_classe()



# Definindo seus atributos
def exibir_atributos(atributos: dict, pontos_livres: int) -> str:
    print('---Vamos definir seus atributos---')
    print(f'Você possui {pontos_livres} para distribuir nesses atributos')
    for atributo, valor in atributos.items():
        print(f'{atributo.capitalize()}: {valor}')
    print(f'[Sair] Escolha feita (Pontos não usados serão perdidos)')

def escolher_atributo(atributos: dict) -> str:
    escolha_atributos = None
    while escolha_atributos not in atributos and escolha_atributos != 'sair':
        escolha_atributos = input('Digite o nome do atributo escolhido: ').lower()
        if escolha_atributos not in atributos and escolha_atributos != 'sair':
            print('Opção incorreta')
    return escolha_atributos

def escolher_add_remove() -> str:
    remover_adicionar = None
    while remover_adicionar not in ['remover', 'adicionar']:
        remover_adicionar = input('Você quer remover ou adicionar pontos? ').lower()
        if remover_adicionar not in ['remover','adicionar']:
            print('Opção incorreta')
    return remover_adicionar

def adicionar_pontos(atributos, escolha_atributos, pontos_livres):
    while True:
        try:
            # Tenta converter a entrada do usuário em um número inteiro
            quantidade_atributo = int(input(f'Quantos pontos de {pontos_livres} você quer adicionar em {escolha_atributos.capitalize()}? '))

            # Verifica se o valor final ultrapassaria 20
            if atributos[escolha_atributos] + quantidade_atributo > 20:
                print(f'Não é possível adicionar essa quantidade. {escolha_atributos.capitalize()} não pode ultrapassar 20.')
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
    quantidade_atributo = int(input(f'Quantos pontos de {pontos_livres} você quer remover em {atributos[escolha_atributos]}? '))
    if atributos[escolha_atributos] - quantidade_atributo >= 0:
        atributos[escolha_atributos] -= quantidade_atributo
        pontos_livres += quantidade_atributo
    else:
        print('Pontos de atributos insuficientes')
    return pontos_livres

def main_atr() -> dict:
    pontos_livres = 27
    atributos = {'forca': 10, 'destreza': 10, 'constituicao': 10, 'inteligencia': 10, 'sabedoria': 10, 'carisma': 10}
    escolha_atributos = None

    while escolha_atributos != 'sair':
        exibir_atributos(atributos, pontos_livres)
        escolha_atributos = escolher_atributo(atributos)
        
        if escolha_atributos != 'sair':
            acao = escolher_add_remove()
            
            if acao == 'adicionar':
                pontos_livres = adicionar_pontos(atributos, escolha_atributos, pontos_livres)
            elif acao == 'remover':
                pontos_livres = remover_pontos(atributos, escolha_atributos, pontos_livres)
    
    print("Distribuição de pontos finalizada!")
    print(f"Atributos finais: {atributos}")
    return atributos

atributos = main_atr()

# Escolhea a arma
def escolher_arma(classe: str):
    if classe == 'Guerreiro':
        armas = warrior.armas
    else:
        armas = {}

    escolha_arma = None
    while escolha_arma not in armas:
        print('---Escolha sua arma---')
        for arma, detalhes in armas.items():
            print(f"{arma} | {detalhes[0]} {detalhes[1]}d{detalhes[2]}")
        escolha_arma = input('Insira o nome da sua arma: ').title()

    return armas[escolha_arma]

arma = escolher_arma(escolha_classe)
print(arma)

# Comece o combate

opcoes_acao = ['Atacar',]

print('---Que o combate comece---')
def escolher_easy() -> list:
    inimigo = easy.randomizar_inimigo()
    return inimigo

def rolagem_iniciativa(destreza: int) -> int:
    des_calculada = floor((destreza - 10) / 2)
    rolagem = random.randint(1, 20)
    iniciativa = des_calculada + rolagem
    return iniciativa

def rolagem_iniciativa_inimigo(destreza_inimigo: int) -> int:
    rolagem = random.randint(1, 20)
    iniciativa = rolagem + destreza_inimigo
    return iniciativa

def primeiro(iniciativa_player: int, iniciativa_inimigo: int) -> str:
    if iniciativa_player >= iniciativa_inimigo:
        primeira_acao = 'player'
    else:
        primeira_acao = 'inimigo'
    return primeira_acao

def calcular_vida(vida_classe: int, constituicao_player: int) -> int:
    cons_calculada = floor((constituicao_player - 10) / 2)
    vida_player = cons_calculada + vida_classe
    return vida_player

def player_atacar(forca_player: int, armadura_inimigo: int, dado: int, dano: int) -> int:
    for_calculada = floor((forca_player - 10) / 2)
    ataque = random.randint(1, 20) + for_calculada
    print(f'A rolagem de ataque foi {ataque}')
    if ataque >= armadura_inimigo:
        dano_total = 0  # Inicialize como zero, não como None
        for n in range(dado):
            dano_rolado = random.randint(1, dano) + for_calculada
            dano_total += dano_rolado
        print(f'O dano total foi: {dano_total}')    
        return dano_total
    else:
        print('O ataque errou')
        return 0

def inimigo_atacar(forca_inimigo: int, armadura_player: int, dado: int, dano: int) -> int:
    ataque = random.randint(1, 20) + forca_inimigo
    print(f'A rolagem de ataque foi {ataque}')
    if ataque >= armadura_player:
        dano_total = 0  # Inicialize como zero, não como None
        for n in range(dado):
            dano_rolado = random.randint(1, dano) + forca_inimigo
            dano_total += dano_rolado
        print(f'O dano total foi: {dano_total}')    
        return dano_total
    else:
        print('O ataque errou')
        return 0
    
def combate_easy():
    inimigo = escolher_easy()
    vida_inimigo = inimigo[1]
    vida_player = calcular_vida(vida_classe, atributos['constituicao'])
    print(f'Seu inimigo é {inimigo[0]}')
    print('Vamos rolar as iniciativas')
    iniciativa_player = rolagem_iniciativa(atributos['destreza'])
    print(f'Sua iniciativa foi: {iniciativa_player}')
    iniciativa_inimigo = rolagem_iniciativa_inimigo(inimigo[4][1])
    print(f'A iniciativa do {inimigo[0]} foi: {iniciativa_inimigo}')
    primeira_acao = primeiro(iniciativa_player, iniciativa_inimigo)
    while vida_inimigo > 0 and vida_player > 0:
        if primeira_acao == 'player':
            escolher_acao = None
            while escolher_acao not in opcoes_acao:
                print('---Seu turno!---')
                print('Atacar')
                escolher_acao = input('Escolha sua ação: ').capitalize()
            if escolher_acao == 'Atacar':
                dano_total = player_atacar(atributos['forca'], inimigo[2], arma[1], arma[2])
                vida_inimigo -= dano_total
                print(f'A vida do seu inimigo é {vida_inimigo}')
            if vida_inimigo <= 0:  # Verificação após o ataque
                break
            print(f'---Turno do {inimigo[0]}---')
            dano_total = inimigo_atacar(inimigo[3][2], armadura_classe, inimigo[3][0], inimigo[3][1])
            vida_player -= dano_total
            print(f'A sua vida é {vida_player}')
        else:
            print(f'---Turno do {inimigo[0]}---')
            dano_total = inimigo_atacar(inimigo[3][2], armadura_classe, inimigo[3][0], inimigo[3][1])
            vida_player -= dano_total
            print(f'A sua vida é {vida_player}')
            if vida_player <= 0:  # Verificação após o ataque
                break
            escolher_acao = None
            while escolher_acao not in opcoes_acao:
                print('---Seu turno---')
                print('Atacar')
                escolher_acao = input('Escolha sua ação: ').capitalize()
            if escolher_acao == 'Atacar':
                dano_total = player_atacar(atributos['forca'], inimigo[2], arma[1], arma[2])
                vida_inimigo -= dano_total
            print(f'A vida do seu inimigo é {vida_inimigo}')

    if vida_inimigo <= 0:
        print(f'O {inimigo[0]} morreu')
        print(f'Você sobreviveu com {vida_player} de HP')
    else:
        print(f'Você morreu')


combate_easy()

