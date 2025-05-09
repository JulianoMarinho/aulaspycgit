# Exercício 1: Criando um dicionário
# Crie um dicionário que armazene informações sobre um livro, como título, autor, ano de 
# publicação e número de páginas. Depois, imprima o dicionário completo.

# Base:
# pessoa = {
#     'nome': 'Felipe',
#     'idade': 25,
#     'profissao': 'Dev',
#     'interesses': ['Python','Programção', 'Mangas'],
#     'pet':{
#         'nome': 'Loki',
#         'idade': 1,
#         'peso': '2kg'
#     }
# }

livros = {
    "titulo": "O nome do vento",
    "autor": "Patrick Rothfuss",
    "ano de publicacao": 2007,
    "numero de paginas": 656
}

# print(livros)

# Exercício 2: Acessando valores
# Dado o dicionário do exercício anterior, acesse e imprima o título e o autor do livro usando as chaves correspondentes.

print(livros["titulo"],livros["autor"])

# Exercício 3: Adicionando um novo par chave-valor
# Adicione a chave "gênero" ao dicionário do exercício 1, com o valor "Ficção Científica", e imprima o dicionário novamente.

livros["genero"] = "Ficção Científica"

print(livros)

# Exercício 4: Alterando um valor
# Altere o valor da chave "número de páginas" para 320 e imprima o dicionário.

livros["numero de paginas"] = 320

print(livros)

# Exercício 5: Removendo um par chave-valor
# Remova a chave "ano de publicação" do dicionário e imprima o dicionário após a remoção.

# saida = livros.pop("ano de publicacao")
# print(saida)
del livros["ano de publicacao"]

# print(livros)

# Exercício 6: Usando o método get()
# Usando o dicionário do exercício 1, tente acessar o valor da chave "preço" usando o método get(). 
# Caso a chave não exista, retorne a mensagem "Chave não encontrada".
# print(livros.get("preço") if livros.get("preço") is not None else "Chave não encontrada")

# Para evitar o get duas vezes, que pode ser ruim em dicionarios maiores, é melhor fazer assim:

preço = livros.get("preço")

print(preço if preço is not None else "Chave não encontrada")


# Exercício 7: Iterando sobre o dicionário
# Dado o dicionário abaixo:

# pessoa = {
#     "nome": "João",
#     "idade": 25,
#     "cidade": "Rio de Janeiro"
# }

# Faça um loop para imprimir todas as chaves e valores do dicionário.

# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")

# Iterando nas chaves

# for chave in pessoa.keys():
#     print(chave)

# Iterando sobre os valores:
# for valor in pessoa.values():
#     print(valor)

print("=" * 40)

# Exercício 8: Contando ocorrências de palavras
# Crie um programa que conte a frequência de cada palavra em uma lista de palavras. 
# Utilize um dicionário para armazenar as palavras como chaves e suas respectivas contagens como valores.

# palavras = ["maçã", "banana", "laranja", "maçã", "maçã", "banana"]

# def conta_palavras(lista):
#     contagem = {}
#     for palavra in lista:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
#     return contagem

# resultado = conta_palavras(palavras)

# print(resultado)

# Exercício 9: Dicionário de listas
# Crie um dicionário onde as chaves são nomes de alunos e os valores são 
# listas com as notas desses alunos. Implemente uma função que calcule a média de cada aluno e imprima o nome do aluno junto com sua média.

# alunos = {
#     "Ana": [10,20,15,30],
#     "Beatriz": [20,10,14,22] 
# }

# def calcula_media(alunos):
#     for chave, valor in alunos.items():
#         media = sum(valor)/ len(valor)
#         print(f"{chave}: média = {media:.2f}")

# calcula_media(alunos)

# teste = ['a', 'b']

# print(len(teste)) # conta quantos elementos tem na lista


# Exercício 10: Trocando chaves e valores
# Dado o dicionário:

# d = {"a": 1, "b": 2, "c": 3}

# def troca_posicoes(dicionario):
#     novo_dicionario = {}
#     for chave, valor in dicionario.items():
#         novo_dicionario[valor] = chave
#     return novo_dicionario

# resultado = troca_posicoes(d)

# print(resultado)

# ✅ Exercício 1: Atualizar valor
# Dado o dicionário:

estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}

estoque["banana"] += 3

print(estoque)

print("=" * 40)

# ✅ Exercício 2: Verificar existência de chave
# Crie um código que verifique se a chave "abacaxi" existe no dicionário 
# estoque. Se não existir, adicione com valor 0.

teste = estoque.get("abacaxi")

if teste == None:
    estoque["abacaxi"] = 0

for chave, valor in estoque.items():
    print(f"{chave}:{valor}")

# ✅ Exercício 3: Remover chave
# Remova a chave "laranja" do dicionário estoque 
# usando o método apropriado.

item_removido = estoque.pop("laranja")

print(f"Foi removido: {item_removido}")

print(f"Novo dicionario: {estoque}")

print("=" * 40)

# ✅ Exercício 4: Soma dos valores
# Dado o dicionário:

vendas = {
    "jan": 1000,
    "fev": 1200,
    "mar": 800
}

def soma_valores(dicionario):
    total = 0
    for valor in dicionario.values():
        total += valor
    return total

soma_das_vendas = soma_valores(vendas)

print(f"A soma das vendas é: {soma_das_vendas}")

print("=" * 40)
# ✅ Exercício 5: Encontrar maior valor
# Com base no dicionário vendas acima, descubra qual mês teve o maior valor de 
# vendas e imprima o mês junto com o valor.

def maior_valor(dicionario):
    valor_comp = 0
    mes = " "
    for chave, valor in dicionario.items():
        if valor > valor_comp:
            valor_comp = valor
            mes = chave
    return mes, valor_comp

print(maior_valor(vendas))