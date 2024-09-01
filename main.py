import random

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


