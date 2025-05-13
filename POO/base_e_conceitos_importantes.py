# Use a Abstração
# Imagine um celular: 
# Marca: Nokia | Modelo: Tijolão | Cor: Azul | 
# Tem câmera: Não | Bateria: Infinita
# Funções do Nokia Tijolão: Fazer ligações, despertador, jogo da cobrinha

# Ex:

class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    tem_camera = False
    bateria = 'Inifinita'

    def fazer_ligacoes(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')
    
    def calcular(self, v1, v2):
        return f'O valor da soma é {v1 + v2}'

# instanciando

celular = Celular()

print(celular.marca)
print(celular.modelo)
print(celular.tem_camera)
print(celular.bateria)

# Executando coisas
print("=" * 40)

celular.fazer_ligacoes()
celular.jogar_cobrinha()
celular.despertador()
calculado = celular.calcular(1,2)
print(calculado)
