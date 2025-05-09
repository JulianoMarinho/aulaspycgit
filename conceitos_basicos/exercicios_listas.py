# Crie uma lista com 5 números inteiros digitados pelo usuário e exiba a soma desses números.

# Aqui teria 2 formas de receber um valor, com map e com laço.

# Com map

# numeros = list(map(int, input("Digite os numeros separados por espaço:").split()))

# Com um laço:

# numeros = []

# for i in range(3):
#     numero = int(input("Digite um número:"))
#     numeros.append(numero)
  
# print(numeros)

# pra somar:

# numeros = list(map(int, input("Digite os numeros separados por espaço: ").split()))

# soma = sum(numeros)

# print(f"A soma dos números é: {soma}")

# Peça 10 números e armazene apenas os pares em uma nova lista. Depois, exiba essa nova lista.

# Forma simples:
# pares = []
# for i in range(10):
#     numero = int(input(f"Digite o {i}º numero:"))
#     if numero % 2 == 0:
#         pares.append(numero)

# print(pares)

# Com compreensão de listas:

# numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(10)]

# pares = [numero for numero in numeros if numero % 2 == 0]

# print(pares)

# Peça 5 nomes ao usuário, armazene em uma lista, e depois mostre essa lista em ordem inversa.

# nomes = [input(f"Digite o {i + 1}º nome:") for i in range(5)]
# nomes.reverse()
# print(f"A lista de nomes invertida é: {nomes}")

# Peça ao usuário para digitar nomes até digitar "sair". 
# Remova todos os nomes que começarem com a letra "A" e imprima a lista resultante.

# nomes = []

# while True:
#     nome = input("Digite um nome ou digite sair para sair:")
#     if nome == 'sair':
#         break
#     else:
#         nomes.append(nome)

# # remover nomes que começam com 'A' ou 'a'

# nomes_filtrados = [nome for nome in nomes if not nome.startswith(('A', 'a'))]

# print(nomes_filtrados)

# Exercícios com Compreensão de Lista

# Crie uma lista com os quadrados dos números de 1 a 10 usando compreensão de lista.

# numeros = [1,2,3,4,5,6,7,8,9,10]

# def numeros_quadrados(numero):
#     return numero ** 2

# quadrados = [numeros_quadrados(numero) for numero in numeros]

# print(f"Lista com os números elevados ao quadrado: {quadrados}")

# Sugestão para lista dos quadrados:

#quadrados = [n ** 2 for n in range(1, 11)]
#print(quadrados)

# Dada a lista numeros = [1, 4, 6, 9, 2, 8], use compreensão de lista para criar uma nova lista apenas com os números maiores que 5

# numeros = [1, 4, 6, 9, 2, 8]

# maiores_que_5 = [numero for numero in numeros if numero > 5]

# print(maiores_que_5)

# Peça uma frase ao usuário e use compreensão de lista para criar uma lista com todas as palavras que tenham mais de 3 letras.

# frase = input("Digite uma frase:")

# palavras = frase.split()

# palavras_maiores = [palavra for palavra in palavras if len(palavra) > 3]

# print(palavras_maiores)

# ============================= EXTRAS ===============================

## Crie uma lista com os quadrados dos números ímpares de 1 a 20 usando compreensão de lista.

# impares = [numero ** 2 for numero in range(1,20) if numero % 2 != 0]

# print(impares)

## Filtrar strings: Dada a lista abaixo:

# nomes = ["Ana", "Bruno", "Amanda", "Carlos", "alberto", "Beatriz"]

# Use compreensão de lista para criar uma nova lista apenas com os nomes que não começam com "A" ou "a".

# nomesA = [nome for nome in nomes if not nome.startswith(('A','a'))]

# # nomes_filtrados = [nome for nome in nomes if not nome.startswith(('A', 'a'))]
# print(nomesA)

# Palavras curtas: Peça ao usuário uma frase e use compreensão de lista para criar uma lista 
# com todas as palavras com 3 letras ou menos.

# frase = input("Digite uma Frase:")

# palavras = frase.split()

# palavras_menores = [palavra for palavra in palavras if len(palavra) <= 3]

# print(palavras_menores)

## Tamanhos de palavras: Peça ao usuário uma frase. Gere uma lista com o comprimento de 
# cada palavra digitada (ex: "Oi tudo bem" → [2, 4, 3]).

# frase = input("Digite uma Frase:")

# palavras = frase.split() 

# palavras_numeros = [len(palavra) for palavra in palavras]

# print(palavras_numeros)

## Números pares em lista aninhada : Dada a lista de listas: listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Crie uma única lista com todos os números pares usando compreensão de lista.

# lista aninhada é uma lista dentro de outra lista, para percorrer tem que fazer 2 fors

# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# pares = [numero for sublista in listas  for numero in sublista if numero % 2 == 0]

# print(pares)

# Lista de booleanos:  Peça 5 números ao usuário e crie uma lista de True ou False indicando se cada número é maior que 10.

# numeros = [int(input(f"Digite o {i + 1}º numero:")) for i in range(0,5)]

# verifica_par = [numero > 10 for numero in numeros]

# print(verifica_par)

## Duplicar vogais: Peça ao usuário uma palavra. Crie uma nova string em que todas as vogais sejam duplicadas. 
# Exemplo: casa → caasaa.

# palavra = input("Digite uma palavra:")

# duplica_vogais = [letra * 2 if letra in 'aeiouAEIOU' else letra for letra in palavra]

# nova_palavra = ''.join(duplica_vogais)

# print(nova_palavra)

#O método .join() transforma uma lista de strings em uma única string. Ele junta todos os elementos 
# da lista, usando como separador o que estiver antes do .join().
# Funciona apenas com listas de strings, então se você tentar usar com números, 
# dá erro — a menos que converta para string antes.

## USO DO JOIN

# Peça ao usuário uma frase e transforme-a em uma lista de palavras. Depois, junte 
# essa lista novamente em uma string com um hífen (-) entre as palavras.

# frase = input("Digite uma frase: ")

# palavras = frase.split()

# com_hifen = '-'.join(palavras)

# print(com_hifen)

# Receba uma palavra do usuário e retorne a palavra com cada letra separada por um espaço.
# Exemplo:
# Entrada: python
# Saída: p y t h o n

# palavra = input("Digite uma palavra: ")

# print(' '.join(palavra))


# Peça uma frase ao usuário. Remova todas as vogais e junte o restante com .join() para formar uma nova string.

# frase = "Ola mundo"

# letras = [letra for letra in frase if letra not in 'AaEeIiOoUu']

# print(letras)

# Peça ao usuário uma frase e inverta a ordem das palavras, mantendo as palavras originais intactas.

# Exemplo:
# Entrada: hoje é um dia lindo
# Saída: lindo dia um é hoje

# frase = "hoje é um dia lindo"

# palavras = frase.split()
# palavras.reverse()

# saida = ' '.join(palavras) # Junta a lista
# print(saida)

# Peça uma palavra e exiba todas as letras separadas por -.

# Exemplo:
# Entrada: casa
# Saída: c-a-s-a

# palavra = input("Digite uma palavra: ")

# saida = '-'.join(palavra)

# print(saida)

# 🔹 Exercício 3 — Juntar palavras com vírgula
# Peça ao usuário uma frase e exiba todas as palavras separadas por vírgula e espaço.

# Exemplo:
# Entrada: amo programar em Python
# Saída: amo, programar, em, Python

# entrada = "amo programar em Python"
# palavras = entrada.split()
# saida = ', '.join(palavras)

# print(saida)

# 🔹 Exercício 4 — Substituir espaços por underline
# Peça uma frase e retorne com os espaços substituídos por _.

# Exemplo:
# Entrada: isso é muito legal
# Saída: isso_é_muito_legal

# entrada = "isso é muito legal"
# palavras = entrada.split()
# saida = '_'.join(palavras)

# print(saida)

# 🔹 Exercício 5 — Somente primeiras letras
# Peça ao usuário uma frase e mostre apenas a primeira letra de cada palavra, separadas por . (ponto).

# Exemplo:
# Entrada: Python é incrível
# Saída: P.é.i

# entrada = "Python é incrível"

# palavras = entrada.split()

# print('.'.join([palavra[0] for palavra in palavras]))


