# Listas são estruturas de dados que armazenam vários valores em uma única variável. 
# Podem conter qualquer tipo de dado (números, strings, etc.), inclusive misturados.

# frutas = ["maçã", "banana", "laranja"]
# numeros = [10, 20, 30, 40]
# mistura = ["texto", 3.14, True, 7]

# # Acessando Elementos:

# print(frutas[0])  # maçã
# print(frutas[-1]) # laranja (último elemento)

# # Modificando Elementos:

# frutas[1] = "uva"
# print(frutas)  # ['maçã', 'uva', 'laranja']

# # Métodos úteis de lista:

# frutas.append("abacaxi")      # adiciona no final
# frutas.insert(1, "kiwi")      # insere na posição 1
# frutas.remove("laranja")      # remove o item
# frutas.pop()                  # remove o último item
# len(frutas)                   # retorna o tamanho

# Exercícios
# Crie uma lista com 5 nomes e imprima todos os nomes, um por linha.

nomes = ['Ana', 'José', 'João', 'Lucas', 'Marcos']

for nome in nomes:
    print(nome, end = '\n')

print("=" * 40)

# Peça para o usuário digitar 3 números e armazene-os em uma lista. Depois, imprima a soma dos números.
numeros = 1
lista = []
soma = 0

while numeros <= 3:
    lista.append(int(input(f"Digite o {numeros}º:")))
    numeros += 1

soma = sum(lista)

print(f"A soma dos números digitados é: {soma}")

print ("=" * 40)

# Peça para o usuário digitar 3 números e, em seguida, calcule a média desses números e informe 
# se a média está abaixo de 5 (reprovado), entre 5 e 7 (recuperação) ou acima de 7 (aprovado).

numeros = list(map(int, input("Digite 3 números separados por espaço: ").split()))

# O input() recebe os números como uma string.

# O método split() divide a string pelos espaços e cria uma lista.

# A função map(int, ...) converte cada item da lista para um número inteiro.

# O sum(numeros) faz a soma diretamente da lista.

media = sum(numeros)/3

if media > 7:
    print("Aprovado")
elif  5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")





