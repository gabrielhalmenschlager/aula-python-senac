
class ContaBancaria:
    def __init__(self, titular, saldoInicial = 0):
        self.titular = titular
        self.saldo = saldoInicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Deposito de R${valor:.2f} realizado. Saldo: R${self.saldo:.2f}')
        else:
            print('Valor invalido')


    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado. Saldo: R${self.saldo:.2f}')
        else:
            print('Valor invalido')

conta = ContaBancaria('Gabriel', 1000)
conta.depositar(500)
conta.sacar(200)