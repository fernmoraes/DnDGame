import random
import warrior
import easy
escolha_arma = None


# Definindo sua classe
op_classes = ['guerreiro']
escolha_classe = None

while escolha_classe not in op_classes:
    print('---Escolha sua Classe---')
    print('Guerreiro')
    print('Futuramente mais')
    escolha_classe = input('Minha classe será: ')
    escolha_classe = escolha_classe.lower()

print(f'Sua classe será {escolha_classe}')


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
    quantidade_atributo = int(input(f'Quantos pontos de {pontos_livres} você quer adicionar em {atributos[escolha_atributos]}? '))
    
    # Verifica se o valor final ultrapassaria 20
    if atributos[escolha_atributos] + quantidade_atributo > 20:
        print(f'Não é possível adicionar essa quantidade. {escolha_atributos.capitalize()} não pode ultrapassar 20.')
    elif pontos_livres - quantidade_atributo >= 0:
        atributos[escolha_atributos] += quantidade_atributo
        pontos_livres -= quantidade_atributo
    else:
        print('Pontos livres insuficientes')
    
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
    atributos = {'força': 10, 'destreza': 10, 'constituicao': 10, 'inteligencia': 10, 'sabedoria': 10, 'carisma': 10}
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
# Escolhendo arma

while escolha_arma not in warrior.armas:
    print('---Escolha sua arma---')
    print(f'Espada Curta | 1d6')
    print(f'Espada Grande | 2d6')
    print(f'Espada Longa | 1d10')
    escolha_arma = input('Insira o nome da sua arma: ').title()

if escolha_arma in warrior.armas:
    arma = warrior.armas[escolha_arma]
print(arma)

# Comece o combate

print('---Que o combate comece---')
def escolher_easy() -> list:
    inimigo = easy.randomizar_inimigo()
    return inimigo

def rolagem_iniciativa(destreza: int) -> int:
    des_calculada = (destreza - 10) / 2
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

def atacar(forca: int, armadura: int, dado: int, dano: int) -> int:
    ataque = random.randint(1, 20) + forca
    print(f'Seu ataque foi {ataque}')
    if ataque >= armadura:
        dano_total = None
        for n in range(dado):
            dano = random.randint(1, dano) + forca
            dano_total += dano
        print(f'Seu dano total foi: {dano_total}')    
        return dano_total
    else:
        print('Seu ataque errou')
        return 0
    
def primeiro_acao():
    inimigo = escolher_easy()
    print(f'Seu inimigo é {inimigo[1]}')
    print('Vamos rolar as iniciativas')
    iniciativa_player = rolagem_iniciativa(atributos['destreza'])
    print(f'Sua iniciativa foi: {iniciativa_player}')
    iniciativa_inimigo = rolagem_iniciativa_inimigo(inimigo[5[2]])
    print(f'A iniciativa do {inimigo[1]} foi: {iniciativa_inimigo}')
    primeira_acao = primeiro(iniciativa_player, iniciativa_inimigo)
    if primeira_acao == 'player':
        escolher_acao = None
        while escolher_acao not in [1, 2]:
            print('Você começa!')
            print('[1] Atacar')
            print('[2] Fugir')
            escolher_acao = int(input('Escolha sua ação: '))
        if primeira_acao == 1:
            atacar(atributos['força'], inimigo[3], )
