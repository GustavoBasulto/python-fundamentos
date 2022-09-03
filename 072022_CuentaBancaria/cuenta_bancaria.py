class CuentaBancaria:
    cuentas=[]
    def __init__(self, tasa_interes=0.10 ,balance=500):
            self.tasa_int = tasa_interes
            self.balance = balance
            CuentaBancaria.cuentas.append(self)
    
    def deposito (self, amount):
        self.balance += amount
        return self
    
    def retiro (self, amount):
        if self.balance<amount:
            print("Saldo insuficiente, retira ", amount, "y su saldo es ", self.balance)
        else:
            self.balance -= amount
        return self

    def mostrar_info_cuenta (self):
        print("balance: ", self.balance, "Interes:", self.tasa_int)
        return self

    def generar_interes (self):
        if self.balance>0:
            inte=self.balance*self.tasa_int
            self.balance=self.balance+inte
        else:
            print("Sin fondos")
        return self
     
    @classmethod
    def info_cta(cls):
        print (cls.balance)
        

cta1 = CuentaBancaria(0.05 , 500)
cta2 = CuentaBancaria(0.05 , 700)

info_cta()

cta1.deposito(200).deposito(100).deposito(400).retiro(500).generar_interes().mostrar_info_cuenta()
cta2.deposito(900).deposito(800).retiro(400).retiro(500).retiro(400).retiro(500).generar_interes().mostrar_info_cuenta()