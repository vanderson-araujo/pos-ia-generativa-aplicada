import subprocess
import os
from dataclasses import dataclass

class JogadaInvalidaException(Exception):
    pass

@dataclass
class Jogador:
    nome: str
    marcador: str

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

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def cadastrar_jogadores():
    while True:
        nome_x = input("Digite o nome do jogador X: ").strip().capitalize()
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
        break


def buscar_jogador_por_marcador(marcador: str) -> Jogador:
    return jogador_x if jogador_x.marcador == marcador else jogador_o

def verifica_vitoria() -> ResultadoVitoria:
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

def limpar_console():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

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

def executa_jogada(jogador: Jogador):
    while True:
        try:
            posicao = solicitar_entrada_jogador(jogador)
            jogar(jogador, posicao)
            break

        except JogadaInvalidaException as e:
            limpar_console()
            mostrar_tabuleiro()
            print(f"Obs: {str(e)}")

def iniciar_rodada():
    ultimo_jogador = None

    while continua_rodada():
        limpar_console()
        mostrar_tabuleiro()

        ultimo_jogador = verifica_jogador_atual(ultimo_jogador)

        executa_jogada(ultimo_jogador)

        resultado = verifica_vitoria()

        if resultado.venceu:
            limpar_console()
            mostrar_tabuleiro()
            print(f"Parabéns {resultado.vencedor.nome}! Você venceu!")
            break

    else:
        limpar_console()
        mostrar_tabuleiro()
        print("Deu velha! Ninguém venceu.")

# main
limpar_console()
cadastrar_jogadores()
iniciar_rodada()