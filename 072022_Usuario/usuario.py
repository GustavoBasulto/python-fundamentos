class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_depósito(self, amount):
        self.balance_cuenta += amount

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    def mostar_balance_usuario(self):
        print("Usuario:", self.name, "- Balance:", self.balance_cuenta)
    
    def transfer_dinero(self, otro, amount):
        self.balance_cuenta -= amount
        otro.balance_cuenta += amount


pedro = Usuario("Pedro Lira", "pedro@hola.com")
juan = Usuario("Juan Lopez", "juan@hola.com")
diego = Usuario("Diego Diaz", "diego@hola.com")

pedro.hacer_depósito(300)
pedro.hacer_depósito(200)
pedro.hacer_depósito(200)
pedro.hacer_retiro(300)
pedro.mostar_balance_usuario()

juan.hacer_depósito(400)
juan.hacer_depósito(200)
juan.hacer_retiro(200)
juan.hacer_retiro(300)
juan.mostar_balance_usuario()

diego.hacer_depósito(800)
diego.hacer_retiro(100)
diego.hacer_retiro(200)
diego.hacer_retiro(50)
diego.mostar_balance_usuario()

pedro.transfer_dinero(diego, 100)
pedro.mostar_balance_usuario()
diego.mostar_balance_usuario()