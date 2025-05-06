import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)

class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.pow(self.base * self.base + self.altura * self.altura, 0.5)

    def tipo_triangulo(self):
        if self.base == self.altura and self.base == self.calcular_hipotenusa() and self.altura == self.calcular_hipotenusa():
            print("Es un triángulo equilátero")
        elif self.base != self.altura and self.base != self.calcular_hipotenusa() and self.altura != self.calcular_hipotenusa():
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")

class PruebaFiguras:

    def __init__(self):
        self.circulo = Circulo(2)
        self.rectangulo = Rectangulo(1,2)
        self.cuadrado = Cuadrado(3)
        self.triangulo_rectangulo = TrianguloRectangulo(3,5)

    def ejecucion(self):
        print(f"El área del círculo es = {self.circulo.calcular_area()}")
        print(f"El perímetro del círculo es = {self.circulo.calcular_perimetro()}")
        print()
        print(f"El área del rectángulo es = {self.rectangulo.calcular_area()}")
        print(f"El perímetro del rectángulo es = {self.rectangulo.calcular_perimetro()}")
        print()
        print(f"El área del cuadrado es = {self.cuadrado.calcular_area()}")
        print(f"El perímetro del cuadrado es = {self.cuadrado.calcular_perimetro()}")
        print()
        print(f"El área del triángulo es = {self.triangulo_rectangulo.calcular_area()}")
        print(f"El perímetro del triángulo es = {self.triangulo_rectangulo.calcular_perimetro()}")
        self.triangulo_rectangulo.tipo_triangulo()

if __name__ == "__main__":
    prueba = PruebaFiguras()
    prueba.ejecucion()
