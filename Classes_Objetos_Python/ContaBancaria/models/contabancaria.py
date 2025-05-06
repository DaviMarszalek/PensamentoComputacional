class ContaBancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.hiostórico = historico
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print(f"Valor {valor} inválido para depósito.")    
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({})
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            a = input(f"Deseja usar o limite de ({self.limite}) para sacar (R${valor}) ? (s para sim)")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print(f"Saque de R${valor} realizado com sucesso!")
                else:
                    print("Saldo e limites insificientes para o saque!")
            else:
                print("Operação com limite cancelada.")        
                
        
        
    def transferir(self):
        
        
        
    def exibir_historico(self)   
    
    
    
    def exibir_saldo(self)       