# Pedra-papel-tesoura Game
Este é um jogo simples de Pedra, Papel e Tesoura, onde o usuário escolhe uma opção e a máquina escolhe outra de forma aleatória. O resultado é exibido e a contagem de vitórias, derrotas e empates é mantida.

## Requisitos
1. Python 3.x
2. Módulo random
## Como jogar
Abra o terminal e execute o arquivo .py
Digite "Pedra", "Papel" ou "Tesoura"
Observe o resultado e a contagem de vitórias, derrotas e empates
Para sair do jogo, digite "Não" ao ser perguntado se deseja continuar jogando
## Variáveis
qt: dicionário que armazena a contagem de vitórias, derrotas e empates
lista: lista de opções de jogo (Pedra, Papel, Tesoura)
res: resposta do usuário
a: resposta aleatória da máquina
i: resposta para continuar jogando ou sair.
## Código
O código utiliza o módulo random para escolher aleatoriamente uma opção e compara com a resposta do usuário. Caso sejam iguais, é registrado um empate. Caso contrário, verifica se a combinação resulta em vitória ou derrota para o usuário. A contagem de resultados é mantida no dicionário "qt". O jogo continua enquanto o usuário desejar.
