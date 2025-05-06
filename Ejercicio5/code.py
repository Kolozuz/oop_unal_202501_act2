from enum import Enum, auto

class tipoCuenta(Enum):
    AHORROS = auto()
    CORRIENTE = auto()

class cuentaBancaria:
    def __init__(self, num_cuenta: int, nombres_titular: str, apellidos_titular: str, tipo_cuenta: tipoCuenta):
        self.num_cuenta = num_cuenta
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0
        
    def imprimir(self):
        for key, val in self.__dict__.items():
            print(f"{key}: {val}")
            
    def consultarSaldo(self):
        print(f"El saldo actual es: ${self.saldo}")
        
    def consignar(self, cantidad: float):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se ha consignado ${cantidad}. El nuevo saldo es: ${self.saldo}")
            return True
        else:
            print("El valor a consignar debe ser mayor a cero.")
            return False
    
    def retirar(self, cantidad: float):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se ha retirado ${cantidad}. El nuevo saldo es: ${self.saldo}")
            return True
        else:
            print("El valor a retirar debe ser mayor a cero y menor o igual al saldo actual.")
            return False

if __name__ == "__main__":
    cuenta_bancaria = cuentaBancaria(123456789, "Pedro", "Perez", tipoCuenta.AHORROS)
    cuenta_bancaria.imprimir()
    cuenta_bancaria.consignar(200000)
    cuenta_bancaria.consignar(300000)
    cuenta_bancaria.retirar(400000)