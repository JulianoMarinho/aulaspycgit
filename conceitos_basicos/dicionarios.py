# lista = ['Um', 'Dois', 'Três']

# meu_dicio = {'nome': 'Felipe', 'idade': 25, 'profissao': 'Dev'}

# # Diferença de lista e discionario, na lista, cada elemento tem um índice e
# # para acessar o item, tem que passar o indice, no dicionario, passa-se a chave
# # Acessando os valores do dicionário:

# print(meu_dicio['nome'])

# #outra forma de acessar valores do discionario, é usando o get

# print(meu_dicio.get('idade'))

# #outro método é o pop

# print(meu_dicio.pop('idade')) #remove o elemento idade de dentro do dicionário

# #listar chaves do dicionário:

# print(meu_dicio.keys())

# # mostrar os valores sem as chaves:
# print(meu_dicio.values())

# # limpar o dicionario:
# print(meu_dicio.clear())

# print("=" * 40)

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

# print(pessoa.get('interesses')[0])

# print(pessoa.get('pet').get('nome'))

# print(pessoa['pet']['nome'])

# pessoa['ano_nascimento'] = 1997

# print(pessoa)

# pessoa['pet']['cor_do_pelo'] = 'Branco'

# print(pessoa)

# pessoa['mae'] = {
#     'nome': 'Maria',
#     'idade': 50
# }

# print(pessoa)

# Um dicionário é representado por chaves {} e contém pares de chave e valor. A chave é única dentro do 
# dicionário, e o valor pode ser de qualquer tipo de dado (string, número, lista, etc.).

# Exemplo de um dicionário simples:

# Definindo um dicionário
meu_dicionario = {
    "nome": "Juliano",
    "idade": 30,
    "cidade": "São Paulo"
}

print(meu_dicionario)

# Você pode acessar os valores usando a chave associada a cada valor.

# Acessando o valor usando a chave
print(meu_dicionario["nome"])  # Saída: Juliano
print(meu_dicionario["idade"])  # Saída: 30

# Você pode adicionar um novo par chave-valor ou alterar um valor existente.

# Adicionando um novo par chave-valor
meu_dicionario["profissão"] = "Desenvolvedor"
print(meu_dicionario)

# Alterando um valor
meu_dicionario["idade"] = 31
print(meu_dicionario)

# Você pode remover um par chave-valor utilizando o comando del ou o método pop.

# Usando 'del' para remover um item
del meu_dicionario["cidade"]
print(meu_dicionario)

# Usando 'pop' para remover e retornar o valor
profissao = meu_dicionario.pop("profissão")
print(profissao)  # Saída: Desenvolvedor
print(meu_dicionario)

# Métodos úteis de dicionário:
# keys(): Retorna todas as chaves do dicionário.

# values(): Retorna todos os valores do dicionário.

# items(): Retorna uma lista de tuplas contendo pares de chave-valor.

# get(): Acessa um valor usando uma chave, mas sem gerar erro se a chave não existir.


# Exemplo de alguns métodos
print(meu_dicionario.keys())    # Saída: dict_keys(['nome', 'idade'])
print(meu_dicionario.values())  # Saída: dict_values(['Juliano', 31])
print(meu_dicionario.items())   # Saída: dict_items([('nome', 'Juliano'), ('idade', 31)])

# Usando o método get()
print(meu_dicionario.get("nome"))  # Saída: Juliano
print(meu_dicionario.get("cidade", "Chave não encontrada"))  # Saída: Chave não encontrada

# Quando usar dicionários?
# Dicionários são ideais quando você precisa associar informações de forma rápida e precisa, com a garantia de que a chave será 
# única e você terá acesso rápido aos valores.

# Exemplos de uso:

# Armazenar dados de um usuário, como nome, idade, e cidade.

# Contar a frequência de palavras em um texto.

# Criar uma lista de preços de produtos, onde cada produto tem uma chave única (nome ou ID) e um valor (preço).

# Se tiver alguma dúvida sobre o uso ou precisar de mais exemplos, só avisar!
