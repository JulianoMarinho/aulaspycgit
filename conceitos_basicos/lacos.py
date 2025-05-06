def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}', end = '\n')

clientes = ['Ana', 'Jonas', 'Felipe']

for i, cliente in enumerate(clientes):
    if i == 2:
        break #interrompe o laço depois de uma condição
    envia_email(cliente)
