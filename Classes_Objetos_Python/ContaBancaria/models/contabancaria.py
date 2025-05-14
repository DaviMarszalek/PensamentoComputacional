import time

class ContaBancaria:
    '''
    Classe que implementa métodos para gerenciar uma conta bancária.add()
    Atributos: titular(string), saldo(float), limite(float) e hostóricos (lista de dicionários)
    
    OBS: Operações no histórico: 0 - sacar, 1 - depositar, 2 - transferir
    '''
    
    def __init__(self, titular: str, saldo: float, limite: float, chaves_pix: list, historico: list) -> None:

        '''
        Construtor da classe ContaBancaria
        '''
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__chaves_pix = chaves_pix
        self.__historico = historico
        
        
    def depositar(self, valor: float) -> bool:
        '''
        Objetivo: Método que realiza o depósito de um valor na conta bancária.
        Entrada: valor (float).
        Return: True se a operação obtiver sucesso. False se a operação não for realizada.
        '''
        if valor > 0:
            self.__saldo += valor
            self.__historico.append({"operacao": 1,
                                   "remetente": self.__titular,
                                   "destinatario": "",
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "dataetempo": int(time.time())})
            print(f"Depósito de R${valor} realizado com sucesso!")
            return True
        else:
            print(f"Valor {valor} inválido para depósito.")   
            return False  
          

    
    
    def sacar(self, valor: float) -> bool:
        '''
        Objetivo: Método que realiza o saque de um valor na conta bancária.
        Entrada: valor (float).
        Return: True se a operação obtiver sucesso. False se a operação não for realizada.
        '''
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append({"operacao": 0,
                                   "remetente": self.__titular,
                                   "destinatario": "",
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "dataetempo": int(time.time())})
            print(f"Saque de R${valor} realizado com sucesso!")
            return True
        else:
            a = input(f"Deseja usar o limite de ({self.__limite}) para sacar (R${valor}) ? (s para sim)")
            if a == 's':
                if (self.__saldo + self.__limite) >= valor:
                    self.__saldo -= valor
                    print(f"Saque de R${valor} realizado com sucesso!")
                    return True
                else:
                    print("Saldo e limite insificientes para o saque!")
            else:
                print("Operação com limite cancelada.")        
        return False        
        

    """
    def depositar(self, valor, remetente = None):
        '''
        Objetivo: Método que realiza o depósito de um valor na conta bancária.
        Entradas: valor (float), remetente(string)
        Return: True se a operação obtiver sucesso. False se a operação não for realizada.
        '''
        op = 1
        if remtente != None:
            op = 2
        if valor > 0:
            self.__saldo += valor
            self.__historico.append({"operacao": op,
                                   "remetente": remtente,
                                   "destinatario": self.__titular,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "dataetempo": int(time.time())})
            print(f"Depósito de R${valor} realizado com sucesso!")
            return True
        else:
            print(f"Valor {valor} inválido para depósito.")   
            return False 
    
    def sacar(self, valor, destinatario = None):
        '''
        Objetivo: Método que realiza o saque de um valor na conta bancária.
        Entradas: valor (float), destinatario(string)
        Return: True se a operação obtiver sucesso. False se a operação não for realizada.
        '''
        op = 0
        if remtente != None:
            op = 2
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append({"operacao": op,
                                   "remetente": self.__titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "dataetempo": int(time.time())})
            print(f"Saque de R${valor} realizado com sucesso!")
            return True
        else:
            a = input(f"Deseja usar o limite de ({self.__limite}) para sacar (R${valor}) ? (s para sim)")
            if a == 's':
                if (self.__saldo + self.__limite) >= valor:
                    self.__saldo -= valor
                    print(f"Saque de R${valor} realizado com sucesso!")
                    return True
                else:
                    print("Saldo e limite insificientes para o saque!")
            else:
                print("Operação com limite cancelada.")        
        return False 
        
        def transferir(self, destinatario, valor):
         
            '''
            Objetivo: Método que realiza a transferência de um valor entre contas bancárias.
            Entradas: destinatario (string), valor (float)
            Return: True se a operação obtiver sucesso. False se a operação não for realizada.
            ''' 
            if self.sacar(valor, destinatario.titular)
                destinatario.depositar(valor, self.__titular)
            """

    def transferir(self, valor: float, destinatario: str) -> bool:
        '''
        Objetivo: Método que realiza a transferência de um valor entre contas bancárias.
        Entradas: valor (float), destinatário (string)
        Return: True se a operação obtiver sucesso. False se a operação não for realizada.
        '''
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append({"operacao": 2,
                                   "remetente": self.__titular,
                                   "destinatario": destinatario.titular,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "dataetempo": int(time.time())})
            print(f"Transferência de R${valor} realizada com sucesso!")
            return True
        else:
           a = input(f"Deseja usar o limite de ({self.__limite}) para sacar (R${valor}) ? (s para sim)")
           if a == 's':
                if (self.__saldo + self.__limite) >= valor:
                    self.__saldo -= valor
                    self.__historico.append({"operacao": 2,
                                   "remetente": self.__titular,
                                   "destinatario": destinatario.titular,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "dataetempo": int(time.time())})
                    print(f"Transferência de R${valor} realizado com sucesso!")
                    return True
                else:
                    print("Saldo e limite insificientes para o transferência!")
           else:
                print("Operação com limite cancelada.")        
        return False         
    
    def exibir_historico(self) -> None:
        print("Histórico de transações:")   
        for transacao in self.__historico:
            dt = time.localtime(transacao["dataetempo"])
            print("Op:", transacao["operacao"],
                  "- Remetente:", transacao['remetente'], 
                  "- Destinatário:", transacao["destinatario"],
                  "- Saldo:", transacao["saldo"],
                  "- Valor:", transacao["valor"],
                  "- Data e Tempo:", f"{dt.tm_mday}/{dt.tm_mon}/{dt.tm_year}", 
                  str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec))   
     
    def exibir_saldo(self) -> None:  
        print(f"Titular: {self.__titular} - Saldo: {self.__saldo} - Limite: {self.__limite}")
        
    def pix(self, valor, chave_pix: list) -> bool:
        '''
        Objetivo: Método que realiza a transferência de um valor entre contas bancárias.
        Entradas: va
        Return: True se a operação obtiver sucesso. False se a operação não for realizada.
        '''
        if chave_pix in self.__chaves_pix:
            return True
        else:
            print("Chave pix não encontrada.")
            return False    
        
    def getTitular(self):
        '''
        Objetivo: Método que retorna o titular da conta bancária sem altera-lo.'''
        return self.__titular
    
    def getChavesPix(self) -> list:
        return self.__chaves_pix
   