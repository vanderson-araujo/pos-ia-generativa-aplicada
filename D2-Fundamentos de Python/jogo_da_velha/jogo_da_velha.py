import os

class JogadaInvalidaException(Exception):
    pass

# Salva os jogadores em dicionários
jogador_atual_x = {"nome": "", "marcador": "X"}
jogador_atual_o = {"nome": "", "marcador": "O"}

# Salva o tabuleiro do jogo da velha como uma lista de listas
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def cadastrar_jogadores():
    """
    Guarda a entrada dos jogadores
    """
    jogador_atual_x["nome"] = input("Digite o nome do jogador X: ").capitalize()
    jogador_atual_o["nome"] = input("Digite o nome do jogador O: ").capitalize()

def verifica_vitoria():
    """
    Verifica se partida possui um ganhador de acordo com as combinações possível

    Returns:
        Tuple: 1: Se partida finalizada, 2: Jogador Vencedor, 3: Combinação completa
    """
    combinacoes = [
        [(0, 0), (0, 1), (0, 2)], # primeira linha horizontal
        [(1, 0), (1, 1), (1, 2)], # segunda linha horizontal
        [(2, 0), (2, 1), (2, 2)], # terceira linha horizontal
        [(0, 0), (1, 0), (2, 0)], # primeira coluna vertical
        [(0, 1), (1, 1), (2, 1)], # segunda coluna vertical
        [(0, 2), (1, 2), (2, 2)], # terceira coluna vertical
        [(0, 0), (1, 1), (2, 2)], # diagonal principal
        [(0, 2), (1, 1), (2, 0)]  # diagonal secundária
    ]

    for combinacao in combinacoes:
        a, b, c = combinacao

        valor_a = tabuleiro[a[0]][a[1]]
        valor_b = tabuleiro[b[0]][b[1]]
        valor_c = tabuleiro[c[0]][c[1]]

        if valor_a != " " and valor_a == valor_b == valor_c:
            return True, buscar_jogador_por_marcador(valor_a), combinacao
    
    return False, None, None

def get_valor_visualizacao(valor, linha, coluna, dados_rodada: tuple[bool, dict | None, list[tuple[int, int]] | None]):
    """
    Define o valor que será  populado na interface
    Args:
        valor: Valor X ou 0
        linha: Linha da jogada
        colluna: Coluna da jogada
        dados_rodada: Informações do status da partida
    """
    is_jogo_finalizado = dados_rodada[0]
    combinacao = dados_rodada[2]

    if is_jogo_finalizado and ((combinacao[0][0] == linha and combinacao[0][1] == coluna) or (combinacao[1][0] == linha and combinacao[1][1] == coluna) or (combinacao[2][0] == linha and combinacao[2][1] == coluna)):
        return f"[{valor}]"
    elif is_jogo_finalizado:
        return f" {valor} " if valor != " " else "   "
    else:
        return f" {valor} " if valor != " " else f"{linha}-{coluna}"

def mostrar_tabuleiro():
    """
    Função para mostrar o tabuleiro do jogo no console
    """
    dados_rodada = verifica_vitoria()

    for index, linha in enumerate(tabuleiro):
        print(
            get_valor_visualizacao(linha[0], index, 0, dados_rodada), 
            get_valor_visualizacao(linha[1], index, 1, dados_rodada), 
            get_valor_visualizacao(linha[2], index, 2, dados_rodada), sep=" | ")

        if (index != len(tabuleiro) - 1):
            print("-" * 15)
    print()

def validar_jogada(jogada: tuple[int, int]):
    """
    Valida se informações de entrada são valores válidos
    Args:
        jogada: Tuple (L, C), ex: (0, 0)
    Raises:
        JogadaInvalidaException: Caso informações de entrada seja inválida
    """
    
    if len(jogada) != 2:
        raise JogadaInvalidaException("Entrada errada, informe L-C, ex: 1-1")

    linha, coluna = jogada
    if linha not in range(3) or coluna not in range(3):
        raise JogadaInvalidaException("Jogada inválida! linha e coluna devem estar entre 0 e 2.")
    
    if (tabuleiro[linha][coluna] != " "):
        raise JogadaInvalidaException(f"Jogada inválida! A posição {jogada} já está ocupada.")

def jogar(jogador_atual, jogada):
    """
    Controla as jogadas dos jogadores
    Args:
        jogador_atual: Jogador que fez a jogada
        jogada: Jogada atual
    """
    validar_jogada(jogada)
    linha, coluna = jogada
    tabuleiro[linha][coluna] = jogador_atual["marcador"]

def buscar_jogador_por_marcador(marcador):
    """
    Busca pelo jogador de acordo com o marcador utilizado

    Args:
        marcador: valor X ou 0 de acordo com o usuário
    """
    if jogador_atual_x["marcador"] == marcador:
        return jogador_atual_x
    else:
        return jogador_atual_o

def is_continua_rodada():
    """
    Verifica se a rodada continua ou finaliza

    Returns:
        Se partida tem continuidade
    """
    for linha in tabuleiro:
        if linha[0] == " " or linha[1] == " " or linha[2] == " ":
            return True
    return False

def limpar_console():
    """
    Faz a limpeza do console
    """
    os.system("cls" if os.name == "nt" else "clear")

def verifica_jogador_atual(ultimo_jogador):
    """
    Verifica qual é o jogador que irá jogar
    
    Returns:
        Jogador que irá fazer a jogada
    """
    if ultimo_jogador == jogador_atual_x:
        return jogador_atual_o
    else:
        return jogador_atual_x
    
def tratar_erro_jogada(jogador, mensagem: str):
    """
    Processo executado quando ocorrer erro na entrada de dados
    """
    limpar_console()
    mostrar_tabuleiro()
    print(f"Obs: {mensagem}")
    executa_jogada(jogador)

def solicitar_entrada_jogador(jogador):
    """
    Solicita a entrada para o jogador da vez

    Args:
        jogador: Jogador da vez

    Returns:
        Tuple com as informações da jogada linha e coluna, ex: (0, 0)
    """
    while True:
        try:
            print(f"Jogador {jogador['nome']} ({jogador['marcador']})")
            print("Informe a linha e a coluna da jogada (ex: 0-1):", end=" ")
            return tuple(map(int, input().split("-")))
        except ValueError:
            limpar_console()
            mostrar_tabuleiro()
            print("Obs: Jogada inválida! Entrada deve ser dois inteiros, ex: 1-2")

def executa_jogada(jogador):
    """
    Responsável por executar a rodada

    Args:
        jogador: Jogador da vez
    """
    while True:
        try:
            jogada = solicitar_entrada_jogador(jogador)
            jogar(jogador, jogada)
            break
        except JogadaInvalidaException as e:
            limpar_console()
            mostrar_tabuleiro()
            print(f"Obs: {str(e)}")

def iniciar_rodada():
    """
    Inicia a rodada
    """
    
    ultimo_jogador = None

    while is_continua_rodada():
        limpar_console()
        mostrar_tabuleiro()
        ultimo_jogador = verifica_jogador_atual(ultimo_jogador)
        
        executa_jogada(ultimo_jogador)

        is_continua, vencedor, combinacao = verifica_vitoria()
        if is_continua:
            limpar_console()
            mostrar_tabuleiro()
            print(f"Parabéns {vencedor['nome']}! Você venceu!")
            break

        if (not is_continua_rodada()):
            break

### main ###
limpar_console()
cadastrar_jogadores()
iniciar_rodada()


