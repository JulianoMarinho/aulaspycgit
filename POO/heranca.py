class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print('Acelerando...')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')

    
# instanciando

carro = Carro()

carro.acelerar()

# herança

class Uno(Carro): #Uno herda -> Carro

    ano = '1992'

uno = Uno()

uno.acelerar()
