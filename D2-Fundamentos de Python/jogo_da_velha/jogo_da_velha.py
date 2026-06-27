import subprocess
import os
from dataclasses import dataclass
from enum import Enum
import random

class TipoJogo(Enum):
    JOGADOR_VS_JOGADOR = (1, "Jogador vs Jogador")
    JOGADOR_VS_IA = (2, "Jogador vs IA")

    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao

    @classmethod
    def por_codigo(cls, codigo: int):
        for tipo in cls:
            if tipo.codigo == codigo:
                return tipo

        raise ValueError("Código inválido.")

class JogadaInvalidaException(Exception):
    pass

@dataclass
class Jogador:
    nome: str
    marcador: str
    isIA: bool = False

class NivelIA(Enum):
    FACIL = 1
    MEDIO = 2
    DIFICIL = 3

@dataclass
class Posicao:
    linha: int
    coluna: int

@dataclass
class ResultadoVitoria:
    venceu: bool
    vencedor: Jogador | None
    combinacao: list[Posicao] | None

jogador_x = Jogador("", "X")
jogador_o = Jogador("", "O")

tipo_jogo: TipoJogo
nivel_ia: NivelIA = NivelIA.FACIL

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

combinacoes = [
    [Posicao(0, 0), Posicao(0, 1), Posicao(0, 2)],
    [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
    [Posicao(2, 0), Posicao(2, 1), Posicao(2, 2)],

    [Posicao(0, 0), Posicao(1, 0), Posicao(2, 0)],
    [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1)],
    [Posicao(0, 2), Posicao(1, 2), Posicao(2, 2)],

    [Posicao(0, 0), Posicao(1, 1), Posicao(2, 2)],
    [Posicao(0, 2), Posicao(1, 1), Posicao(2, 0)]
]

def jogada_ia_facil():
    jogadas = []

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                jogadas.append(Posicao(linha, coluna))

    return random.choice(jogadas)

def jogada_ia_medio() -> Posicao:
    print("Aguarde a jogada da IA ...")
    # 1. Se a IA puder vencer, vence
    posicao = encontrar_jogada_vencedora("O")
    if posicao is not None:
        return posicao

    # 2. Se o jogador puder vencer, bloqueia
    posicao = encontrar_jogada_vencedora("X")
    if posicao is not None:
        return posicao

    # 3. Se o centro estiver livre, joga no centro
    if tabuleiro[1][1] == " ":
        return Posicao(1, 1)

    # 4. Caso contrário, primeira posição livre
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                return Posicao(linha, coluna)

def jogada_ia_dificil() -> Posicao:

    # tenta vencer
    jogada = encontrar_jogada_vencedora("O")
    if jogada is not None:
        return jogada

    # bloqueia
    jogada = encontrar_jogada_vencedora("X")
    if jogada is not None:
        return jogada

    # centro
    if tabuleiro[1][1] == " ":
        return Posicao(1, 1)

    # cantos
    cantos = [
        Posicao(0,0),
        Posicao(0,2),
        Posicao(2,0),
        Posicao(2,2)
    ]

    livres = [
        p for p in cantos
        if tabuleiro[p.linha][p.coluna] == " "
    ]

    if livres:
        return random.choice(livres)

    # laterais
    laterais = [
        Posicao(0,1),
        Posicao(1,0),
        Posicao(1,2),
        Posicao(2,1)
    ]

    livres = [
        p for p in laterais
        if tabuleiro[p.linha][p.coluna] == " "
    ]

    return random.choice(livres)
  
def encontrar_jogada_vencedora(marcador: str) -> Posicao | None:
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = marcador

                resultado = verifica_vitoria()

                tabuleiro[linha][coluna] = " "

                if resultado.venceu:
                    return Posicao(linha, coluna)

    return None

def limpar_console():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

def escolher_nivel_ia():
    limpar_console()

    while True:
        try:
            print("Selecione o nível de dificuldade:")
            for nivel in NivelIA:
                print(f"{nivel.value} - {nivel.name}", sep="\n")
            
            return NivelIA(int(input("\nEscolha: ")))
            break
        except ValueError:
            limpar_console()
            print("Obs: Escolha entre as opçoes informada")

def escolher_tipo_jogo():
    global tipo_jogo
    global nivel_ia

    while True:
        try:
            for tipo in TipoJogo:
                print(f"{tipo.codigo}-{tipo.descricao}", sep="\n")

            tipo_jogo = TipoJogo.por_codigo(int(input("Opção: ")))

            if TipoJogo.JOGADOR_VS_IA == tipo_jogo:
                nivel_ia = escolher_nivel_ia()

            break
        except ValueError:
            limpar_console()
            print("Obs: Escolha entre as opçoes informada")

def cadastrar_jogadores():
    while True:
        nome_x = input("Digite o nome do jogador X: ").strip().capitalize()

        if tipo_jogo == TipoJogo.JOGADOR_VS_IA:
            nome_o = "IA"
        else:
            nome_o = input("Digite o nome do jogador O: ").strip().capitalize()

        if nome_x == "" or nome_o == "":
            limpar_console()
            print("Obs: O nome do jogador não pode ser vazio.")
            continue

        if nome_x.casefold() == nome_o.casefold():
            limpar_console()
            print("Obs: O nome dos jogadores não pode ser igual.")
            continue

        jogador_x.nome = nome_x
        jogador_o.nome = nome_o
        jogador_o.isIA = tipo_jogo == TipoJogo.JOGADOR_VS_IA
        break


def buscar_jogador_por_marcador(marcador: str) -> Jogador:
    return jogador_x if jogador_x.marcador == marcador else jogador_o

def verifica_vitoria() -> ResultadoVitoria:
    for combinacao in combinacoes:
        a, b, c = combinacao

        valor_a = tabuleiro[a.linha][a.coluna]
        valor_b = tabuleiro[b.linha][b.coluna]
        valor_c = tabuleiro[c.linha][c.coluna]

        if valor_a != " " and valor_a == valor_b == valor_c:
            return ResultadoVitoria(
                True,
                buscar_jogador_por_marcador(valor_a),
                combinacao
            )

    return ResultadoVitoria(False, None, None)


def posicao_esta_na_combinacao(posicao: Posicao, combinacao: list[Posicao]) -> bool:
    return posicao in combinacao


def get_valor_visualizacao(
    valor: str,
    posicao: Posicao,
    resultado: ResultadoVitoria
) -> str:

    if resultado.venceu and resultado.combinacao is not None:
        if posicao_esta_na_combinacao(posicao, resultado.combinacao):
            return f"[{valor}]"

        return f" {valor} " if valor != " " else "   "

    return f" {valor} " if valor != " " else f"{posicao.linha}-{posicao.coluna}"


def mostrar_tabuleiro():
    resultado = verifica_vitoria()

    for indice_linha, linha in enumerate(tabuleiro):
        print(
            get_valor_visualizacao(linha[0], Posicao(indice_linha, 0), resultado),
            get_valor_visualizacao(linha[1], Posicao(indice_linha, 1), resultado),
            get_valor_visualizacao(linha[2], Posicao(indice_linha, 2), resultado),
            sep=" | "
        )

        if indice_linha != len(tabuleiro) - 1:
            print("-" * 15)

    print()


def validar_jogada(posicao: Posicao):
    if posicao.linha not in range(3) or posicao.coluna not in range(3):
        raise JogadaInvalidaException(
            "Jogada inválida! linha e coluna devem estar entre 0 e 2."
        )

    if tabuleiro[posicao.linha][posicao.coluna] != " ":
        raise JogadaInvalidaException(
            f"Jogada inválida! A posição {posicao.linha}-{posicao.coluna} já está ocupada."
        )

def jogar(jogador: Jogador, posicao: Posicao):
    validar_jogada(posicao)
    tabuleiro[posicao.linha][posicao.coluna] = jogador.marcador

def continua_rodada() -> bool:
    for linha in tabuleiro:
        if " " in linha:
            return True

    return False

def verifica_jogador_atual(ultimo_jogador: Jogador | None) -> Jogador:
    if ultimo_jogador == jogador_x:
        return jogador_o

    return jogador_x

def solicitar_entrada_jogador(jogador: Jogador) -> Posicao:
    while True:
        try:
            print(f"Jogador {jogador.nome} ({jogador.marcador})")
            print("Informe a linha e a coluna da jogada (ex: 0-1):", end=" ")

            linha, coluna = map(int, input().split("-"))

            return Posicao(linha, coluna)

        except ValueError:
            limpar_console()
            mostrar_tabuleiro()
            print("Obs: Jogada inválida! Entrada deve ser dois inteiros, ex: 1-2")

def jogada_ia():
    match nivel_ia:
        case NivelIA.FACIL:
            return jogada_ia_facil()

        case NivelIA.MEDIO:
            return jogada_ia_medio()

        case NivelIA.DIFICIL:
            return jogada_ia_dificil()

        case NivelIA.IMPOSSIVEL:
            return jogada_ia_minimax()

def executa_jogada(jogador: Jogador):
    while True:
        try:
            if jogador.isIA:
                posicao = jogada_ia()
            else:
                posicao = solicitar_entrada_jogador(jogador)

            jogar(jogador, posicao)
            break

        except JogadaInvalidaException as e:
            limpar_console()
            mostrar_tabuleiro()
            print(f"Obs: {str(e)}")

def iniciar_rodada():
    ultimo_jogador = random.choice([jogador_x, jogador_o])

    while continua_rodada():
        limpar_console()
        mostrar_tabuleiro()

        ultimo_jogador = verifica_jogador_atual(ultimo_jogador)

        executa_jogada(ultimo_jogador)

        resultado = verifica_vitoria()

        if resultado.venceu:
            limpar_console()
            mostrar_tabuleiro()
            if tipo_jogo == TipoJogo.JOGADOR_VS_IA and resultado.vencedor.isIA:
                print("Parece que hoje você foi promovido a pato de IA.")
                print("Não desanime... até os melhores já perderam para um monte de ifs.")
            elif tipo_jogo == TipoJogo.JOGADOR_VS_IA and not resultado.vencedor.isIA:
                print(f"Parabéns {resultado.vencedor.nome}! Você venceu!")
                print("Mas convenhamos, eu deixei você ganhar só para não desanimar logo na primeira tentativa.")
                print("Na próxima eu jogo sério.")
            else:
                print(f"Parabéns {resultado.vencedor.nome}! Você venceu!")
            break

    else:
        limpar_console()
        mostrar_tabuleiro()
        print("""
        Deu velha!

        Achou que ia ser fácil?
        Nem você ganhou... nem a IA.

        Pelo menos ninguém vai dormir se achando o campeão hoje.
        """)

# main
limpar_console()
escolher_tipo_jogo()
cadastrar_jogadores()
iniciar_rodada()