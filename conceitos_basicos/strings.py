texto = 'Meu texto'
print(type(texto))
#Uma string é uma cadeia de caracteres.
print(texto[0])

#capturar um trecho da cadeia de caracter
print(texto[0:3])

print(texto[0:]) #pega até o final da string

print(texto[:4]) #pega do primeiro caracter até o último

print(len(texto)) #retonar o tamanho da string

print(texto.count('e',0,11)) #retonar quantas recorrências são encontrads na string

print(texto.find('Meu')) #retorna a posição em que o trecho começa na string

print(texto.upper()) #coloca o texto da string em caixa alta

print(texto.lower()) #coloca o texto em minusculo

print(texto.capitalize()) #coloca a primeira letra do texto em maiusculo

print(texto.title()) #deixa o texto em formato de título com a primeira letra de cada palavra maiuscula

print(texto.split())
lista_de_palavras = texto.split()
resultado = '-'.join(lista_de_palavras)
print(resultado)

texto2 = ' Aula pycode '
print(texto.strip()) #limpa os espaços no início e no fim

#rstrip() remove os espaços da direita
#lstrip() remove todos os espaços da esquerda

