import numpy as np

tabuleiro = [[[] for _ in range(4)] for _ in range(4)]
jogador = [0, 0]
ouro_pego = False
wumpus_vivo = True
flecha_usada = False
pontos = 0

def menu():
    print("""
        Comandos disponíveis:
        - cima --> andar para cima
        - baixo --> andar para baixo
        - esquerda --> andar para esquerda
        - direita --> andar para direita
        - pegar --> pegar o ouro
        - atirar --> atirar a flecha
        - inventario --> ver o inventário
        - ajuda --> ver as regras do jogo
        - sair --> desistir do jogo
        """)
    
def ajuda():
    print("""
        Ajuda:
        O objetivo do jogo é pegar o ouro, matar o Wumpus e voltar para a casa inicial (0, 0) sem ser comido ou cair em um buraco. 
        Você pode andar, pegar o ouro, atirar a flecha e ver seu inventário. O Wumpus e os buracos estão escondidos no tabuleiro, mas você pode sentir o fedor e a brisa quando estiver perto deles. 
        Você tem \033[91muma flecha\033[m e deve usá-la para matar o Wumpus.
        Você começa com 0 pontos e pode ganhar ou perder pontos ao longo do jogo.
        Cada vez que você tentar sair do tabuleiro ou fizer um movimento inválido, você perderá pontos.
        Você pode usar o comando \033[91minventario\033[m para ver quantos pontos você tem e se pegou o ouro ou usou a flecha.
        Você pode usar o comando \033[91majuda\033[m a qualquer momento para ver as regras do jogo novamente.
        Você pode sair do jogo a qualquer momento digitando \033[91msair\033[m.
        --> Boa sorte!
        """)

def adiciona_mapa(i, j, percepcao):
    if percepcao not in tabuleiro[i][j]:
        tabuleiro[i][j].append(percepcao)

def mostra_percepcao(i, j):
    casa = tabuleiro[i][j]
    percep =  []
    if 'F' in casa:
        percep.append("Você sente um fedor.")
    if 'V' in casa:
        percep.append("Você sente uma brisa.")
    if 'O' in casa:
        percep.append("Você vê ouro.")
    if not casa:
        percep.append("Você não sente nada.")
    print("\n".join(percep))

    return 

def pegar_ouro():
    global ouro_pego, pontos
    if 'O' in tabuleiro[jogador[0]][jogador[1]]:
        ouro_pego = True
        print("Você pegou o ouro!")
        pontos += 100
        tabuleiro[jogador[0]][jogador[1]].remove('O')
        return True
    else:
        print("Não há ouro aqui.")
        pontos -= 5

    return False

def usar_flecha(i, j):
    global wumpus_vivo, flecha_usada, pontos
    if 0 <= i < 4 and 0 <= j < 4:
        if 'W' in tabuleiro[i][j] and not flecha_usada:
            wumpus_vivo = False
            print("O Wumpus foi morto!")
            pontos += 100
            tabuleiro[i][j].remove('W')
            flecha_usada = True
            for x, y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                if 0 <= x < 4 and 0 <= y < 4 and 'F' in tabuleiro[x][y]:
                    tabuleiro[x][y].remove('F')

            if ouro_pego == True:
                print("Você pode voltar para a casa inicial e ganhar o jogo!")
        else:
            print("Você não acertou o Wumpus.")
            pontos -= 10
            flecha_usada = True
    else:
        print("Você não pode atirar fora do tabuleiro, perdeu sua flecha.")
        flecha_usada = True
        pontos -= 5

def andar(comando):
    global jogador, pontos
    i, j = jogador

    if comando == 'cima':
        i_novo = i - 1
        j_novo = j
    elif comando == 'baixo':
        i_novo = i + 1
        j_novo = j
    elif comando == 'esquerda':
        i_novo = i
        j_novo = j - 1
    elif comando == 'direita':  
        i_novo = i
        j_novo = j + 1
    else:
        print("Comando inválido.")
        pontos -= 5
    
    if 0 <= i_novo < 4 and 0 <= j_novo < 4:
        jogador = [i_novo, j_novo]
        print(f"Você se moveu para a casa ({i_novo}, {j_novo}).")
        mostra_percepcao(i_novo, j_novo)
        
        if 'W' in tabuleiro[i_novo][j_novo]:
            print("Você foi comido pelo Wumpus!")
            pontos -= 100
            print(f"Pontos: {pontos}")
            return False
        elif 'B' in tabuleiro[i_novo][j_novo]:
            print("Você caiu em um buraco!")
            pontos -= 50
            print(f"Pontos: {pontos}")
            return False
    else:
        print("Você não pode sair do tabuleiro.")
        pontos -= 5
        jogador = [i, j]
        print(f"Você ainda está na casa ({i}, {j}).")
        return True

def inventario():
    global flecha_usada, ouro_pego, pontos
    print("Você tem:")
    if ouro_pego:
        print("- Ouro")
    if not flecha_usada:
        print("- 1 flecha")
    print(f"- {pontos} pontos.")

# posiciona o Wumpus no tabuleiro, sem ser na posição inicial (0, 0)
w1, w2 = np.random.randint(0,4), np.random.randint(0,4)
while (w1, w2) == (0, 0):
    w1, w2 = np.random.randint(0,4), np.random.randint(0,4)
adiciona_mapa(w1, w2, 'W')

# adiciona o fedor nas casas adjacentes ao Wumpus, cima, baixo, esquerda e direita se estiverem dentro do tabuleiro
for f1, f2 in [[w1-1, w2], [w1+1, w2], [w1, w2-1], [w1, w2+1]]:
    if 0 <= f1 < 4 and 0 <= f2 < 4:
        adiciona_mapa(f1, f2, 'F')

# adiciona o ouro no tabuleiro, sem ser na posição inicial (0, 0) e sem ser na posição do Wumpus
o1, o2 = np.random.randint(0, 4), np.random.randint(0, 4)
while (o1, o2) == (w1, w2) or (o1, o2) == (0, 0):
    o1, o2 = np.random.randint(0, 4), np.random.randint(0, 4)
adiciona_mapa(o1, o2, 'O')

# adiciona 4 buracos diferentes no tabuleiro, sem ser na posição inicial (0, 0) e sem ser na posição do Wumpus ou do ouro
buracos = []

while len(buracos) < 4:
    b1, b2 = np.random.randint(0, 4), np.random.randint(0, 4)
    while (b1, b2) == (0, 0):
        b1, b2 = np.random.randint(0, 4), np.random.randint(0, 4)
    if 'O' not in tabuleiro[b1][b2] and 'W' not in tabuleiro[b1][b2] and [b1, b2] not in buracos:
        adiciona_mapa(b1, b2, 'B')
        buracos.append([b1, b2])

# adiciona as brisas nas posições adjacentes aos buracos, cima, baixo, esquerda e direita se estiverem dentro do tabuleiro	
for i, j in buracos:
    for v1, v2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if 0 <= v1 < 4 and 0 <= v2 < 4:
            adiciona_mapa(v1, v2, 'V')


# mostra o tabuleiro inicial
# for linha in tabuleiro:
#     print(["".join(sorted(casa)) if casa else '-' for casa in linha])


# inicia o jogo
print("-"*80)
print("Bem-vindo ao jogo do Wumpus!")

# chama a função menu para explicar os comandos disponíveis
print("-"*80)
menu()

# posiciona o jogador na casa inicial e mostra a percepção inicial
print("-"*80)
print("Você está na casa (0, 0).")
mostra_percepcao(0,0)
print("-"*80)

op = input("Digite o comando: ").strip().lower()
while True:

    # comandos de movimento
    if op in ['cima', 'baixo', 'esquerda', 'direita']:
        if andar(op) == False:
            break

    # comandos de pegar o ouro e atirar a flecha
    elif op == 'pegar':
        if pegar_ouro():
            if flecha_usada == False:
                print("Você deve usar a flecha para matar o Wumpus.")
            else:
                print("Volte para a casa inicial para ganhar o jogo!")

    elif op == 'atirar':
        if flecha_usada == False:
            direcao = input("Para onde você quer atirar? (cima, baixo, esquerda, direita): ").strip().lower()
            if direcao == 'cima':
                usar_flecha(jogador[0]-1, jogador[1])
            elif direcao == 'baixo':
                usar_flecha(jogador[0]+1, jogador[1])
            elif direcao == 'esquerda':
                usar_flecha(jogador[0], jogador[1]-1)
            elif direcao == 'direita':
                usar_flecha(jogador[0], jogador[1]+1)
            else:
                print("Direção inválida.")
        else:
            print("Você já usou a flecha.")

    # comando de visualizar o inventário
    elif op == 'inventario':
        inventario()
    
    # comando de ajuda, ver regras do jogo
    elif op == 'ajuda':
        ajuda()

    elif op == 'sair':
        print("Você desistiu!")
        pontos -= 50
        inventario()
        break
    else:
        print("Comando inválido.")

    # verifica se o jogador ganhou o jogo, cumpriu todos os requisitos
    if ouro_pego == True and jogador == [0, 0] and wumpus_vivo == True:
        print("Você deve matar o Wumpus antes de voltar para a casa inicial.")

    elif ouro_pego == False and jogador == [0, 0] and wumpus_vivo == False:
        print("Você deve pegar o ouro antes de voltar para a casa inicial.")

    elif ouro_pego == False and wumpus_vivo == True and jogador == [0, 0]:
        print("Você deve pegar o ouro e matar o Wumpus antes de voltar para a casa inicial.")

    elif ouro_pego == True and wumpus_vivo == False and jogador == [0, 0]:
            print("Você ganhou o jogo!")
            print(f"Você fez {pontos} pontos.")
            print("Parabéns!")
            break
    
    print("-"*80)
    op = input("Digite o comando: ").strip().lower()
    if op == 'sair':
        print("Você desistiu!")
        pontos -= 50
        inventario()
        break

print("Fim do jogo.")
print("Tabuleiro final:")
for linha in tabuleiro:
    print(["".join(sorted(casa)) if casa else '-' for casa in linha])
