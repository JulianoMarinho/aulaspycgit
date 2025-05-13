class Forma():

    def area(self):
        pass # usado para deixar uma funcao vazia

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado
    # método construtor da classe dunder init

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2
    
quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(f" A área do quadrado 1 é igual a: {area_quadrado}")

quadrado2 = Quadrado(7)
area_quadrado2 = quadrado2.area()
print(f" A área do quadrado 2 é igual a: {area_quadrado2}")

circulo = Circulo(2)
area_circulo = circulo.area()
print(f"A área do círculo é igual a: {area_circulo}")