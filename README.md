
# Jogo de Combate por Turnos - Versão Beta

Este é um jogo de combate por turnos, onde o jogador escolhe uma classe, distribui atributos, escolhe uma arma e enfrenta inimigos em batalhas baseadas em turnos. Atualmente, o jogo está na fase beta e novas funcionalidades serão adicionadas em versões futuras.

## Funcionalidades

- Escolha de classe: Atualmente disponível apenas o **Warrior**.
- Distribuição de atributos: O jogador pode distribuir pontos em força, velocidade, constituição e magia.
- Combate por turnos: O jogador enfrenta inimigos, realiza ataques e tenta sobreviver.
- Escolha de dificuldade: Apenas o modo **easy** está disponível no momento.
- Inimigos aleatórios: Cada combate apresenta um inimigo aleatório, com diferentes atributos e habilidades.

## Como Jogar

1. **Escolha sua classe**: Atualmente, apenas a classe **Warrior** está disponível.
2. **Distribua seus atributos**: Você tem 14 pontos livres para distribuir entre os atributos de força, velocidade, constituição e magia.
3. **Escolha sua arma**: Selecione uma arma que melhor se adapte ao seu estilo de jogo.
4. **Enfrente inimigos**: Participe de combates por turnos contra inimigos aleatórios. Utilize suas habilidades e atributos para derrotar os oponentes.

### Exemplo de Jogo

```bash
---Escolha sua Classe---
Warrior
Minha classe será: warrior
Sua classe será warrior

---Vamos definir seus atributos---
Você possui 14 pontos para distribuir nesses atributos
Strength: 10
Speed: 10
Body: 10
Magic: 10
Digite o nome do atributo escolhido: strength
Você quer remover ou adicionar pontos? add
Quantos pontos de 14 você quer adicionar em Strength? 5
...

---Escolha sua arma---
Espada Curta | Espada Curta 1d6
Espada Grande | Espada Grande 2d6
Espada Longa | Espada Longa 1d10
Insira o nome da sua arma: espada longa

---Escolha a dificuldade dos encontros---
Easy
Dificuldade: easy
```

## Estrutura do Projeto

- `main.py`: Arquivo principal que contém a lógica do jogo.
- `warrior.py`: Contém informações e atributos específicos da classe Warrior.
- `easy.py`: Contém a lista de inimigos e lógica para selecionar inimigos aleatórios.

## Planejamento Futuro

- Adição de novas classes e armas.
- Implementação de novos níveis de dificuldade.
- Expansão da variedade de inimigos.
- Criação de um sistema de habilidades especiais.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.
