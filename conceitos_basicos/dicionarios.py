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

pessoa = {
    'nome': 'Felipe',
    'idade': 25,
    'profissao': 'Dev',
    'interesses': ['Python','Programção', 'Mangas'],
    'pet':{
        'nome': 'Loki',
        'idade': 1,
        'peso': '2kg'
    }
}

print(pessoa.get('interesses')[0])

print(pessoa.get('pet').get('nome'))

print(pessoa['pet']['nome'])

pessoa['ano_nascimento'] = 1997

print(pessoa)

pessoa['pet']['cor_do_pelo'] = 'Branco'

print(pessoa)

pessoa['mae'] = {
    'nome': 'Maria',
    'idade': 50
}

print(pessoa)