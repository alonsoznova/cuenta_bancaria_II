class CuentaBancaria:
    cuentas_bancarias = []
    def __init__(self, tasa_interes = 0.01 , balance = 0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas_bancarias.append(self)
    
    def deposito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        self.balance -= amount
        if(self.balance - amount < 0):
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def generar_interes(self):
        if(self.balance > 0):
            self.balance += self.balance * self.tasa_interes
        return self
    
    @classmethod 
    def imprimir_instancias(cls):
        for x in cls.cuentas_bancarias:
            x.mostrar_info_cuenta()

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = CuentaBancaria(tasa_interes = 0.02, balance = 0)
        print(f"Usuario registrado")

    def hacer_deposito(self, amount):
        self.cuenta.balance += amount
        return self
    
    def hacer_retiro(self, amount):
        self.cuenta.balance -= amount
        return self
    
    def mostrar_balance_cuenta(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.cuenta.balance} ")
        return self
    
    
    def transfer_dinero(self, other_user, amount):
        self.cuenta.retiro(amount)
        other_user.hacer_deposito(amount)
        return self

usuario1 = Usuario("Martín")
usuario2 = Usuario("Paloma")

usuario1.mostrar_balance_cuenta()



