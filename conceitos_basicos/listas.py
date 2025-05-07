# # # Listas são estruturas de dados que armazenam vários valores em uma única variável. 
# # # Podem conter qualquer tipo de dado (números, strings, etc.), inclusive misturados.

# # # frutas = ["maçã", "banana", "laranja"]
# # # numeros = [10, 20, 30, 40]
# # # mistura = ["texto", 3.14, True, 7]

# # # # Acessando Elementos:

# # # print(frutas[0])  # maçã
# # # print(frutas[-1]) # laranja (último elemento)

# # # # Modificando Elementos:

# # # frutas[1] = "uva"
# # # print(frutas)  # ['maçã', 'uva', 'laranja']

# # # # Métodos úteis de lista:

# # # frutas.append("abacaxi")      # adiciona no final
# # # frutas.insert(1, "kiwi")      # insere na posição 1
# # # frutas.remove("laranja")      # remove o item
# # # frutas.pop()                  # remove o último item
# # # len(frutas)                   # retorna o tamanho

# # # Exercícios
# # # Crie uma lista com 5 nomes e imprima todos os nomes, um por linha.

# # nomes = ['Ana', 'José', 'João', 'Lucas', 'Marcos']

# # for nome in nomes:
# #     print(nome, end = '\n')

# # print("=" * 40)

# # # Peça para o usuário digitar 3 números e armazene-os em uma lista. Depois, imprima a soma dos números.
# # numeros = 1
# # lista = []
# # soma = 0

# # while numeros <= 3:
# #     lista.append(int(input(f"Digite o {numeros}º:")))
# #     numeros += 1

# # soma = sum(lista)

# # print(f"A soma dos números digitados é: {soma}")

# # print ("=" * 40)

# # # Peça para o usuário digitar 3 números e, em seguida, calcule a média desses números e informe 
# # # se a média está abaixo de 5 (reprovado), entre 5 e 7 (recuperação) ou acima de 7 (aprovado).

# # numeros = list(map(int, input("Digite 3 números separados por espaço: ").split()))

# # # O input() recebe os números como uma string.

# # # O método split() divide a string pelos espaços e cria uma lista.

# # # A função map(int, ...) converte cada item da lista para um número inteiro.

# # # O sum(numeros) faz a soma diretamente da lista.

# # media = sum(numeros)/3

# # if media > 7:
# #     print("Aprovado")
# # elif  5 <= media < 7:
# #     print("Recuperação")
# # else:
# #     print("Reprovado")

# # Tipos de estruturas de dados: Listas, Tuplas, Sets e dicionários

# carros = []

# carros.append('Marea')

# print(carros)

# carros.append('Fusca')

# print(carros)

# #para adicionar em determinada posição

# carros.insert(1, 'Escort')

# print(carros)

# #remover o ultimo elemento da lista pop, outra forma é o del,
# #ele remove o elemente do indice passado, outro é o remove,
# #ele remove pelo valor, ex: carros.remove('Fusca')

# # del carros[1]

# # carros.count('Fusca') retorna quantas ocorrencias ele encontrou
# # desse elemento, na lista.
# # reverse => carros.reverse() inverte a ordem dos elementos da lista
# # sort => organiza os elementos da melhor forma, no nosso exemplo,
# # carros.sort() organiza os elementos em ordem alfabética

# # Compreensão de listas com python

# # - É um recurso do python emq ue você consegue aplicar uma expressão
# # ou uma função para cada um dos itens de uma lista, retornando assim
# # uma nova lista com os itens alterados conforme a expressão/função que
# # foi executada neles. Ex.: [expr for item in lista] em outras palavras
# # aplique a expressão expr em cada item da lista. A primeira coisa é a 
# # função, ou expressão que você deseja colocar na lista, para cada item na lista

# numeros = [1,2,3,4,5]

# def dobro(numero):
#     return numero * 2

# numeros_dobrados = [dobro(numero) for numero in numeros]

# print(numeros_dobrados) # [2, 4, 6, 8, 10]

nomes = ['Ana', 'Felipe', 'João', 'Arlindo']

nomes_maiusculos = [nome.upper() for nome in nomes]

print(nomes_maiusculos)

# Compreensão de listas com condicional

nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'A']
# se a primeira letra do nome for A, é case sensitive

# ai fica [expr for item in lista cond] 
# "Aplique a expressão expr em cada item da lista que atende a condição cond"
print(nomes_maiusculos)





