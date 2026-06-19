def atividade_pratica_1():
    numero = int(input())

    print("antecessor:", numero - 1)
    print("numero....:", numero)
    print("sucessor..:", numero + 1)

# Efetuar a leitura de três valores inteiros e apresentar o valor do meio.
def atividade_pratica_2():
    a = int(input())
    b = int(input())
    c = int(input())

    if a <= b <= c or c <= b <= a:
        print("meio =", b)
    elif b <= a <= c or c <= a <= b:
        print("meio =", a)
    else:
        print("meio =", c)

# Escreva um programa que monte uma matriz figura para um valor ímpar obtido. A diagonal principal com o caractere @.
def atividade_pratica_3():
    n = int(input())

    for i in range(n):
        for j in range(n):
            if i == j:
                if j == 0:
                    print("@", end="")
                else:
                    print(" @", end="")
            else:
                # caso seja o primeiro elemento não colocar espaço antes do ponto
                if j == 0: 
                    print(".", end="")
                else:
                    print(" .", end="")
        print()

# Leia do teclado 8 (oito) valores inteiros, no intervalo de 0 até 99, e os armazene em um vetor. Em seguida, deverão ser impressos na tela o menor elemento desse vetor.
def atividade_pratica_4():
    numeros: list[int] = []

    for i in range(8):
        numero = int(input())
        if 0 <= numero <= 99:
            numeros.append(numero)
        else:
            continue

    for indice, numero in enumerate(numeros):
        print(f"a[{indice}] = {numero}")

    menor_numero = min(numeros)
    print()
    print(f"Menor valor = {menor_numero}")

# Desenvolva um programa que leia uma string do teclado e a seguir mostre os caracteres na ordem inversa.
def atividade_pratica_5():
    string = input()
    string_invertida = string[::-1]

    print(f"Entrada: {string}")
    print(f"Saida..: {string_invertida}")

#atividade_pratica_5()

def atividade_pratica_22(a, b, c, p_meio):
    if a <= b <= c or c <= b <= a:
        meio = b
    elif b <= a <= c or c <= a <= b:
        meio = a
    else:
        meio = c

    print("meio =", meio)
    if (meio != p_meio):
        print("ERRO: meio deveria ser", p_meio)


atividade_pratica_22(1, 2, 3, 2)
atividade_pratica_22(1, 3, 2, 2)
atividade_pratica_22(2, 1, 3, 2)
atividade_pratica_22(2, 3, 1, 2)
atividade_pratica_22(3, 1, 2, 2)
atividade_pratica_22(3, 2, 1, 2)