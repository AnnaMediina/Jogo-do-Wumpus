# 🏹 Mundo do Wumpus - Versão Terminal

Este projeto é uma implementação em Python de uma releitura do jogo "O Mundo do Wumpus". O jogador deve explorar um mundo, encontrar o ouro, matar o Wumpus e retornar com segurança à posição inicial para vencer!

## 🎯 Objetivo do Jogo

- 🟡 Encontrar e pegar o ouro.
- 🐉 Matar o Wumpus com uma única flecha.
- 🏠 Voltar para a casa inicial (0, 0) com o ouro e o Wumpus morto.

## 📦 Funcionalidades

- Geração aleatória do tabuleiro (4x4) com:
  - 1 Wumpus
  - 1 ouro
  - 4 buracos
- Percepções do ambiente:
  - **Fedor (F)** perto do Wumpus
  - **Brisa (V)** perto de buracos
- Sistema de pontuação e penalidades
- Comandos de texto simples para movimentação e ações

## 🖥️ Tecnologias Utilizadas

- Python 3.x
  -  biblioteca NumPy
  
## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/mundo-do-wumpus.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd mundo-do-wumpus
   ```

3. Execute o jogo no terminal:
   ```bash
   python wumpus.py
   ```

> É necessário ter Python 3 e a biblioteca NumPy instalada:
```bash
pip install numpy
```

## 🎮 Comandos Disponíveis

- `cima` → andar para cima  
- `baixo` → andar para baixo  
- `esquerda` → andar para esquerda  
- `direita` → andar para direita  
- `pegar` → pegar o ouro  
- `atirar` → atirar a flecha  
- `inventario` → ver pontos, ouro e flecha  
- `ajuda` → mostrar instruções do jogo  
- `sair` → desistir do jogo  

## 🧠 Lógica do Jogo

- O tabuleiro é uma matriz 4x4 com posições ocultas.
- O jogador começa na posição (0, 0).
- O Wumpus e os buracos matam instantaneamente.
- O ouro deve ser pego e o Wumpus morto para vencer.
- Percepções indicam perigos próximos, mas não revelam posições diretamente.
- A pontuação é acumulada ou perdida conforme suas ações.

## 📸 Exemplo de Tabuleiro Final

```plaintext
['-', 'F', 'O', '-']
['V', '-', 'V', 'F']
['-', 'B', '-', 'W']
['-', 'V', 'F', '-']
```

## 🏆 Vitória

Você vence ao:
1. Pegar o ouro
2. Matar o Wumpus
3. Retornar para (0, 0)

E o jogo mostrará:
> "Você ganhou o jogo!  
> Você fez X pontos.  
> Parabéns!"

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✍️ Autor

Desenvolvido por [Seu Nome].  
Sinta-se livre para abrir issues, propor melhorias ou contribuir!
```

---

Se quiser, posso criar a versão em inglês também, ou incluir imagens/prints se você for tirar algum print do terminal. Quer que eu gere um `README.md` pronto pra copiar e colar?
