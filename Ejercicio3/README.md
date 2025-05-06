# Ejercicio 2.3 (p.74)

## Diagrama de Clases

![image](https://github.com/user-attachments/assets/0814cb41-78b5-458c-bf55-e18c599e4f99)




### Implementación en código (Python)

```py
from enum import Enum

class Combustible(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIÉSEL"
    BIODIESEL = "BIODIÉSEL"
    GAS_NATURAL = "GAS NATURAL"

class Tipo(Enum):
    CARRO_CIUDAD = "CARRO DE CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"

class Automovil:

    def _init_(self, marca, modelo, motor, tipo_combustible, tipo_automovil, puertas, asientos, velocidad_max, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_max = velocidad_max
        self.color = color
        self.velocidad_actual = 0

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def get_puertas(self):
        return self.puertas

    def get_asientos(self):
        return self.asientos

    def get_velocidad_max(self):
        return self.velocidad_max

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def set_puertas(self, puertas):
        self.puertas = puertas

    def set_asientos(self, asientos):
        self.asientos = asientos

    def set_velocidad_max(self, velocidad_max):
        self.velocidad_max = velocidad_max

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento_velocidad):
        if self.velocidad_actual + incremento_velocidad < self.velocidad_max:
            self.velocidad_actual = self.velocidad_actual + incremento_velocidad
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil")

    def desacelerar(self, decremento_velocidad):
        if self.velocidad_actual - decremento_velocidad > 0:
            self.velocidad_actual = self.velocidad_actual - decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def tiempo_llegada(self, distancia):
        return distancia/self.velocidad_actual

    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor}")
        print(f"Tipo de combustible: {self.tipo_combustible.value}")
        print(f"Tipo de automóvil: {self.tipo_automovil.value}")
        print(f"Número de puertas: {self.puertas}")
        print(f"Cantidad de asientos: {self.asientos}")
        print(f"Velocidad máxima: {self.velocidad_max}")
        print(f"Color: {self.color.value}")

auto_1 = Automovil("Ford", 2018, 3, Combustible.DIESEL, Tipo.EJECUTIVO, 5, 6, 250, Color.NEGRO)
auto_1.imprimir()
auto_1.set_velocidad_actual(100)
print(f"Velocidad actual: {auto_1.get_velocidad_actual()}")
auto_1.acelerar(20)
print(f"Velocidad actual: {auto_1.get_velocidad_actual()}")
auto_1.desacelerar(50)
print(f"Velocidad actual: {auto_1.get_velocidad_actual()}")
auto_1.frenar()
print(f"Velocidad actual: {auto_1.get_velocidad_actual()}")
auto_1.desacelerar(20)
```
