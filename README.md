# 🏹 Mundo do Wumpus - Versão Terminal

Este projeto é uma implementação em Python de uma releitura do jogo "O Mundo do Wumpus". O jogador deve explorar um mundo, encontrar o ouro, matar o Wumpus e retornar com segurança à posição inicial para vencer!

### Objetivo do Jogo

- Encontrar e pegar o ouro.
- Matar o Wumpus com uma única flecha.
- Voltar para a casa inicial (0, 0) com o ouro e o Wumpus morto.

### Funcionalidades

- Geração aleatória de um tabuleiro (4x4) com:
  - 1 Wumpus
  - 1 ouro
  - 4 buracos
- Percepções do ambiente:
  - **Fedor (F)** perto do Wumpus
  - **Brisa (V)** perto de buracos
- Sistema de pontuação e penalidades
- Comandos de texto para movimentação e ações

### Tecnologias Utilizadas

- Python 3.11.5
  -  biblioteca NumPy

### Comandos Disponíveis

- `cima` → andar para cima  
- `baixo` → andar para baixo  
- `esquerda` → andar para esquerda  
- `direita` → andar para direita  
- `pegar` → pegar o ouro  
- `atirar` → atirar a flecha  
- `inventario` → ver pontos, ouro e flecha  
- `ajuda` → mostrar instruções do jogo  
- `sair` → desistir do jogo  

### Lógica do Jogo

- O jogador começa na posição (0, 0).
- O Wumpus e os buracos matam instantaneamente.
- O ouro deve ser pego e o Wumpus morto para vencer.
- Percepções indicam perigos próximos.
- A pontuação é acumulada ou perdida conforme suas ações.

### Exemplo de Tabuleiro

![image](https://github.com/user-attachments/assets/72f84f9a-18b6-444a-b89f-41d3bbe2a316)

### Vitória

Você vence ao:
1. Pegar o ouro
2. Matar o Wumpus
3. Retornar para (0, 0)

