idade = int(input("Digite a sua idade:"))
renda = float(input("Digite sua renda:"))

if idade >= 21 and renda >= 2500:
    print("Pode financiar um carro")
else: 
    print("Não pode financiar um carro")

print ("=" * 40)

idade2 = int(input("Digite sua idade:"))

if idade2 < 12:
    print("Criança")
elif  12 <= idade2 <= 17:
    print("Adolecente")
elif 18 <= idade2 <= 59:
    print("Adulto")
else: 
    print("Idoso")

print("=" * 40)

numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))

def verifica_numero(n, nome):
    if n > 0:
        print(f'O {nome} numero é positivo')
    elif n < 0:
        print(f'O {nome} numero é negativo')
    else:
        print(f'O {nome} numero é zero')

print(f'{verifica_numero(numero1, 'primeiro')} e o {verifica_numero(numero2, 'segundo')}')
    


