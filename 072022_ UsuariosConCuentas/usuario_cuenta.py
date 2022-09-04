class CuentaBancaria:
    cuentas=[]
    def __init__(self, tasa_interes=0.10 ,balance=500):
            self.tasa_int = tasa_interes
            self.balance = balance
            CuentaBancaria.cuentas.append(self)
    
    
    def generar_interes (self):
        if self.balance>0:
            inte=self.balance*self.tasa_int
            self.balance=self.balance+inte
        else:
            print("Sin fondos")
        return self       

class Usuario:
    def __init__(self, name, email, tasa, balance):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa, balance)

    def hacer_depósito(self, amount):
        self.cuenta.balance += amount
        return self

    def hacer_retiro(self, amount):
        if self.cuenta.balance<amount:
            print("Saldo insuficiente, retira ", amount, "y su saldo es ", self.cuenta.balance)
        else:
            self.cuenta.balance -= amount
        return self

    def mostar_balance_usuario(self):
        print("Usuario:", self.name, "- Balance:", self.cuenta.balance, "- Tasa Int:", self.cuenta.tasa_int)
        return self
    
    def transfer_dinero(self, otro, amount):
        self.cuenta.balance -= amount
        otro.cuenta.balance += amount
        return self

pedro = Usuario("Pedro Lira", "pedro@hola.com", 0.05, 500)
diego = Usuario("Diego Diaz", "diego@hola.com", 0.06, 800)

pedro.hacer_depósito(300).hacer_depósito(200).hacer_depósito(200).hacer_retiro(1300).cuenta.generar_interes()#al llamar al atributo de la clase CuentaBancaria continua trabajando sobre esa clase, por lo que ya no encuentra el metodo de la clase usuario
pedro.mostar_balance_usuario()

pedro.transfer_dinero(diego, 100)
pedro.mostar_balance_usuario()
diego.mostar_balance_usuario()
