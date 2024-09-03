import random
import warrior
import easy

''' Definindo sua classe '''
op_classes = ['guerreiro']
escolha_classe = None

while escolha_classe not in op_classes:
    print('---Escolha sua Classe---')
    print('Guerreiro')
    print('Futuramente mais')
    escolha_classe = input('Minha classe será: ')
    escolha_classe = escolha_classe.lower()

print(f'Sua classe será {escolha_classe}')


''' Definindo seus atributos '''
def exibir_atributos(atributos: dict, pontos_livres: int) -> str:
    print('---Vamos definir seus atributos---')
    print(f'Você possui {pontos_livres} para distribuir nesses atributos')
    for atributo, valor in atributos.items():
        print(f'{atributo.capitalize()}: {valor}')
    print(f'[Sair] Escolha feita (Pontos não usados serão perdidos)')

def escolher_atributo(atributos: dict) -> str:
    escolha_atributos = input('Digite o nome do atributo escolhido: ').lower()
    if escolha_atributos in atributos or escolha_atributos == 'sair':
        return escolha_atributos
    else:
        print("Atributo inválido. Tente novamente.")
        return None

def escolher_acao() -> str:
    remover_adicionar = None
    while remover_adicionar not in ['remover', 'adicionar']:
        remover_adicionar = input('Você quer remover ou adicionar pontos? ').lower()
    return remover_adicionar

def adicionar_pontos(atributos: dict, escolha_atributos: str, pontos_livres: int) -> int:
    quantidade_atributo = int(input(f'Quantos pontos de {pontos_livres} você quer adicionar em {atributos[escolha_atributos]}? '))
    if pontos_livres - quantidade_atributo >= 0:
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
            acao = escolher_acao()
            
            if acao == 'adicionar':
                pontos_livres = adicionar_pontos(atributos, escolha_atributos, pontos_livres)
            elif acao == 'remover':
                pontos_livres = remover_pontos(atributos, escolha_atributos, pontos_livres)
    
    print("Distribuição de pontos finalizada!")
    print(f"Atributos finais: {atributos}")

main_atr()

print('Atributos escolhidos')