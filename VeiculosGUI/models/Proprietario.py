class Proprietario:
    
    def __init__(self, nome: str, CPF: str, placa: str, veiculo: str):
        
        self.__nome = nome
        self.__cpf = CPF
        self.__placa = placa
        self.__veiculo = veiculo
        
    def __str__(self) -> str:
        
        infos = f"Nome: {self.__nome}\n"
        infos += f"CPF: {self.__cpf}\n"
        infos += f"Placa: {self.__placa}\n"
        infos+= f"Veículo: {self.__veiculo}"
        
        
        
    
    i    