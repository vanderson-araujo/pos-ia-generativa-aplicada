''' 
Faça um programa para ler um valor monetário (R$) de um produto e calcule um desconto fixo de 10%. 
Calcule também o valor final do produto. Apresente os valores como apresentado na coluna "Resultados".
'''
def atividade_avaliativa_1():
    valor_produto = float(input())

    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto

    print(f"Valor do Produto  = R$ {valor_produto:.2f}")
    print(f"Valor do Desconto = R$ {desconto:.2f}")
    print(f"Valor Final       = R$ {valor_final:.2f}")

''' 
Faça um programa que leia um valor inteiro do teclado (variável "item") e a seguir 
implemente a rotina de busca sequencial: do primeiro elemento da Lista até encontrar; ou até o final da Lista 
e não encontrar. Mostre as posições juntas dos respectivos elementos da Lista "a" e, 
finalizando, com o resultado da busca: encontrou na posição tal; ou não encontrou "item" na Lista "a". 
Observe o resultado final na coluna "Resultados".
'''
def atividade_avaliativa_2():
    item = int(input())
    a: list[int] = [10, 2, 7, 8, 5, 3, 22, 17, 18]

    resultado = "{"

    for i, valor in enumerate(a):
        resultado += f"{i}:{valor}"
        
        if i < len(a) - 1:
            resultado += ", "

    resultado += "}"

    print(resultado)
    print()

    if item in a:
        posicao = a.index(item)
        print(f"Item: {item}, foi encontrado na posicao {posicao}.")
    else:
        print(f"Item: {item}, \"nao\" foi encontrado.")

''' 
Faça um programa para ler um valor monetário (R$) de um produto e calcule um desconto de 10% se o valor do produto for 
inferior a R$ 5.000,00; o desconto a ser calculado, em caso contrário, deverá ser de 15%. 
Calcule, também, o valor final do produto e apresente os valores como mostrado na coluna 'Resultados'.
'''
def atividade_avaliativa_3():
    valor_produto = float(input())

    if valor_produto < 5000:
        vlr_desconto = valor_produto * 0.10
        desconto_aplicado = 10
    else:
        vlr_desconto = valor_produto * 0.15
        desconto_aplicado = 15

    valor_final = valor_produto - vlr_desconto

    print(f"Valor do Produto        = R$ {valor_produto:.2f}")
    print(f"Valor do Desconto ({desconto_aplicado}%) = R$ {vlr_desconto:.2f}")
    print(f"Valor Final             = R$ {valor_final:.2f}")

''' 
Faça um programa para ler um número inteiro que representa o tamanho de uma matriz quadrada. 
Apresente esta matriz como mostrado na coluna "Resultados". Observe que as bordas da matriz são feitas por 
asteriscos (*) e a parte central por símbolos de arroba (@).
'''
def atividade_avaliativa_4():
    n = int(input())

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                if j == 0:
                    print("*", end="")
                else:
                    print(" *", end="")
            else:
                if j == 0:
                    print("@", end="")
                else:
                    print(" @", end="")
        print()

'''
Faça um programa para ler uma String e apresente todos os caracteres desta String 3 (três) vezes na tela do computador. 
Observe o resultado final na coluna "Resultados".
'''
def atividade_avaliativa_5():
    string = input()

    for i in range(3):
        for j, char in enumerate(string):
            if j == 0:
                print(char, end="")
            else:
                print(" " + char, end="")
        print()
        
'''
Faça um programa para ler uma String e apresente todos as palavras desta String. Leve em consideração que entre as palavras 
existem um, e somente um, caractere espaço. Veja, também, que o ponto final não faz parte da última palavra. Observe o 
resultado final na coluna "Resultados".
'''
def atividade_avaliativa_6():
    string = input()
    string = string.replace(".", "")

    palavras = string.split()

    print(f"Existem {len(palavras)} palavras, são elas:")
    print()
    for indice, palavra in enumerate(palavras, start=1):
        print(f"{indice}a. palavra = {palavra}")

'''
Faça um programa para ler um valor inteiro que representa o tamanho de uma Lista e a seguir atribua para as posicões 
pares desta lista o valor 0 (zero) e para as posições ímpares o valor 1 (um). Finalizando, mostre os valores da Lista 
como mostrado na coluna 'Resultados'.
'''
def atividade_avaliativa_7():
    n = int(input())

    print("{", end="")
    for i in range(n):
        if (i != 0 and i < n):
            print(", ", end="")
        
        if i % 2 == 0:
            print(0, end="")
        else:
            print(1, end="")
    print("}")

'''
Faça um programa para ler do teclado 7 (sete) valores inteiros e os armazene em uma Lista. Em seguida, 
deverão ser mostrados na tela do computador: todos os elementos da Lista em ordem ascendente e os menor e maior 
elementos desta Lista com as suas respectivas posições. Observe o resultado final na coluna "Resultados".
'''
def atividade_avaliativa_8():
    numeros: list[int] = []

    for i in range(7):
        numero = int(input())
        numeros.append(numero)

    numerosOrdenados = sorted(numeros)
    for indice, numero in enumerate(numerosOrdenados):
        print(f"x[{indice}] = {numero}")

    print()

    menor_numero = min(numeros)
    maior_numero = max(numeros)

    posicao_menor = numeros.index(menor_numero)
    posicao_maior = numeros.index(maior_numero)

    print(f"Menor elemento, x[{posicao_menor}] = {menor_numero}") 
    print(f"Maior elemento, x[{posicao_maior}] = {maior_numero}")

'''
Faça um programa para ler um valor inteiro (variável "a") e a seguir construa uma Lista com 10 (dez) posições (variável "x") 
com o resultado da seguinte expressão:
x[i] = a + i; para todo "i" variando de 0 até 9.

Observe o resultado final na coluna “Resultados”.
'''
def atividade_avaliativa_9():
    a = int(input())
    x: list[int] = []

    for indice, i in enumerate(range(10)):
        x.append(a + i)
        print(f"x[{i}] = {a} + {i} = { a + indice}")

'''
Faça um programa para ler um valor inteiro que representa o tamanho (variável "n") de uma primeira Lista e a seguir leia 
todos os “n” elementos desta Lista. E, também, construa uma segunda lista onde seus elementos são assim definidos: a) 
se o elemento da primeira lista for um valor negativo, armazenar na segunda lista o valor -1 (menos um); b) se o 
elemento da primeira lista for o valor neutro (zero), armazenar na segunda lista o valor 0 (zero); e, c) se o elemento 
da primeira lista for um valor positivo, armazenar na segunda lista o valor 1 (um). Finalizando, mostre os valores das 
Listas como mostrado na coluna 'Resultados'.
'''
def atividade_avaliativa_10():
    n = int(input())
    lista1: list[int] = []
    lista2: list[int] = []

    for i in range(n):
        numero = int(input())
        lista1.append(numero)

        if numero < 0:
            lista2.append(-1)
        elif numero == 0:
            lista2.append(0)
        else:
            lista2.append(1)

    print("[", end="")
    for indice, numero in enumerate(lista1):
        if indice == 0:
            print(numero, end="")
        else:
            print(", " + str(numero), end="")
    print("]")

    print("[", end="")
    for indice, numero in enumerate(lista2):
        if indice == 0:
            print(numero, end="")
        else:
            print(", " + str(numero), end="")
    print("]")

atividade_avaliativa_10()