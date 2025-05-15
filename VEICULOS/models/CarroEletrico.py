from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    '''
    Classe que representa um carro elétrico
    Argumento: Classe pai Veiculo
    '''
    
    def __init__(self, placa: str, modelo: str, marca: str,
                 ano: int, cor: str, valor_fipe: float,
                 nAssentos: int, nPortas: int, nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        
        Veiculos().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
        
    def __str__(self) -> str:
        infos = Veiculos().__str__()
        infos += f"Número de Assentos: {self.__nAssentos}\n" 
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Nível de Bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo de Bateria: {self.__tipo_bateria}\n"    
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos
    
    def get_nivel_bateria(self) -> int:
        '''
        Retorna o nível de bateria do carro elétrico
        '''
        return self.__nivel_bateria
    
    def get_tipo_bateria(self) -> str:
        return self.__tipo_bateria
    
    def get_autonomia(self) -> int:
        return self.__autonomia
        
        