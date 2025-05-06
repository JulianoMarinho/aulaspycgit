def somar(a,b):
    resultado = a + b
    return resultado

print(somar(1,2))

print("=" * 40)

def boas_vindas(nome):
    print(f"Seja bem-vindo(a), {nome}")

boas_vindas("Juliano")

print("=" * 40)

def media(n1, n2):
    print(f"A média de {n1} e {n2} é igual a {(n1 + n2)/2}")

media(2,4)

print("=" * 40)

def par_impar(n):
    if n%2 == 0:
        print(f"O número {n} é par")
    else:
        print(f"O número {n} é impar")

par_impar(2)

print("=" * 40)

def soma_quadrados(a,b):
    return (a ** 2 + b ** 2)

resultado = soma_quadrados(2,2)

print(f"A soma dos quadrados dos números é: {resultado}")

print("=" * 40)

def eh_bissexto(ano):
    return True if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else False
    
print(eh_bissexto(2025))  

print("=" * 40)

def classificar_media(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"
    
print(classificar_media(10))