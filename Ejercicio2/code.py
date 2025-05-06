from enum import Enum

class Tipo(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    nombre = None
    cantidad_satelites = 0
    masa = 0
    volumen = 0
    diametro = 0
    distancia = 0
    observable = False

    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia, tipo, observable):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia = distancia
        self.tipo = tipo
        self.observable = observable

    def imprimir(self):
        print(f"Nombre del planeta: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa del planeta: {self.masa}")
        print(f"Volumen del planeta: {self.volumen}")
        print(f"Diámetro del planeta: {self.diametro}")
        print(f"Distancia al sol: {self.distancia}")
        print(f"Tipo de planeta: {self.tipo.value}")
        print(f"Es observable: {self.observable}")

    def calcular_densidad(self):
        return self.masa/self.volumen

    def exterior(self):
        limite = 149597870 * 3.4
        if self.distancia > limite:
            return True
        else:
            return False

planeta1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, Tipo.TERRESTRE, True)
planeta1.imprimir()
print(f"Densidad del planeta: {planeta1.calcular_densidad()}")
print(f"Es planeta exterior: {planeta1.exterior()}")

print()

planeta2 = Planeta("Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750000000, Tipo.GASEOSO, True)
planeta2.imprimir()
print(f"Densidad del planeta: {planeta2.calcular_densidad()}")
print(f"Es planeta exterior: {planeta2.exterior()}")
