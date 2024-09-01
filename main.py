import random

# ''' Definindo sua classe '''
# op_classes = ['guerreiro']
# escolha_classe = None

# while escolha_classe not in op_classes:
#     print('---Escolha sua Classe---')
#     print('Guerreiro')
#     print('Futuramente mais')
#     escolha_classe = input('Minha classe será: ')
#     escolha_classe = escolha_classe.lower()

# print(f'Sua classe será {escolha_classe}')


''' Definindo seus atributos '''
pontos_livres = 27
atributos = {'força': 10, 'destreza': 10, 'constituicao': 10, 'inteligencia': 10, 'sabedoria': 10, 'carisma': 10}
escolha_atributos = None
remover_adicionar = None

while escolha_atributos != 'sair':
    remover_adicionar = None
    escolha_atributos = None
    print('---Vamos definir seus atributos---')
    print(f'Você possui {pontos_livres} para distribuir nesses atributos')
    print(f'Força: {atributos['força']}')
    print(f'Destreza: {atributos['destreza']}')
    print(f'Constituição: {atributos['constituicao']}')
    print(f'Inteligência: {atributos['inteligencia']}')
    print(f'Sabedoria: {atributos['sabedoria']}')
    print(f'Carisma: {atributos['carisma']}')
    print(f'[Sair] Escolha feita (Pontos não usados serão perdidos)')
    escolha_atributos = input('Digite o nome do atributo escolhido: ')
    escolha_atributos = escolha_atributos.lower()

    if escolha_atributos in atributos:
        while remover_adicionar != 'remover' and remover_adicionar != 'adicionar':
            print(f'---{escolha_atributos}---')
            print(f'Você possui {atributos[escolha_atributos]} em {escolha_atributos}')
            print(f'Você possui {pontos_livres} para gastar')
            print(f'Você quer remover ou adicionar pontos?')    #Colocar minimo de 10 pontos e máximo de 20 pontos
            remover_adicionar = input('Escolha: ')
            remover_adicionar = remover_adicionar.lower()
        if remover_adicionar == 'adicionar':
            print(f'Quantos pontos de {pontos_livres} você quer adicionar em {atributos[escolha_atributos]}?')
            quantidade_atributo = int(input('Escolha: '))
            if pontos_livres-quantidade_atributo >= 0:
                atributos[escolha_atributos] += quantidade_atributo
                pontos_livres -= quantidade_atributo
            else:
                print('Pontos livres insuficientes')
        if remover_adicionar == 'remover':
            print(f'Quantos pontos de {pontos_livres} você quer remover em {atributos[escolha_atributos]}?')
            quantidade_atributo = int(input('Escolha: '))
            if atributos[escolha_atributos]-quantidade_atributo >= 0:
                atributos[escolha_atributos] -= quantidade_atributo
                pontos_livres += quantidade_atributo
            else:
                print('Pontos de atributos insuficientes')


print('Atributos escolhidos')