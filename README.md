# 🏹 Mundo do Wumpus - Versão Terminal

Este projeto é uma implementação em Python de uma releitura do jogo "O Mundo do Wumpus". O jogador deve explorar um mundo cheio de armadilhas com o objetivo de capturar o ouro, matar o Wumpus e retornar à posição inicial em segurança.

### 🎯 Objetivo do Jogo

- 🪙 Encontrar e pegar o ouro.
- ☠️ Eliminar o Wumpus com uma única flecha.
- 🏠 Retornar à casa inicial (0, 0) com o ouro e o Wumpus morto.

### Funcionalidades

- 🗺️ Gerar um tabuleiro e preenchê-lo aleatoriamente com:
  - 🐉 1 Wumpus (W)
  - 🕳️ 4 buracos (B)
  - 🪙 1 ouro (O)
  - Percepções:
    - 💨 Fedor (F) - indicando Wumpus próximo
    - 🍃 Brisa (V) - indicando buracos próximos
- Sistema de pontuação baseado nas ações do jogador.
- Uma flecha disponível para eliminar o Wumpus.
  
### 🧑‍💻 Tecnologias Utilizadas

- Python 3.11.5
  -  Biblioteca NumPy
 
### 🎮 Como Jogar

1. Abra o seu terminal 🖥️
2. Clone esse repositório:
   ```bash
   git clone https://github.com/AnnaMediina/Jogo-do-Wumpus.git
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd Jogo-do-Wumpus
   ```
4. Instale a biblioteca necessária:
   ```bash
   pip install numpy
   ```
5. Execute o jogo:
   ```bash
   python wumpus.py

### 📸 Exemplo de Tabuleiro Inicial

![image](https://github.com/user-attachments/assets/72f84f9a-18b6-444a-b89f-41d3bbe2a316)

### ⚙️ Como Funciona o Jogo

O jogador move-se pelo tabuleiro levando em consideração as percepções que ele tem em cada casa. A sua missão é encontrar e pegar o ouro, matar o Wumpus com uma única flecha no seu inventário e voltar a casa inicial (0, 0) sem cair em nehum buraco pelo caminho.

Ao atirar a flecha ela viaja em linha reta até a casa adjacente na direção de sua escolha, se o Wumpus estiver lá ele é eliminado e desaparece do tabuleiro, juntamente com seu fedor.

Os comandos possíveis são:
- `cima` --> ir para cima
- `baixo` --> ir para baixo
- `esquerda` --> ir para a esquerda
- `direita` --> ir para a direita
- `pegar` --> pegar o ouro
- `atirar` --> atirar sua flecha
- `inventario` --> ver o inventário e os pontos
- `ajuda` --> ver as regras do jogo
- `sair` --> se quiser desistir do jogo

### 📸 Exemplo de Tabuleiro Final

![image](https://github.com/user-attachments/assets/a220e88e-9a2d-481d-b139-a3e70ead9c63)
