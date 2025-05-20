from .Veiculos import Veiculos

class Carro(Veiculos):
    
    def __init__(self, placa: str, modelo: str, marca: str,
                    ano: int, cor: str, valor_fipe: float, eficiencia: int) -> None:
            
            Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        
            self.__eficiencia = eficiencia
   
    def calcular_consumo(self, distancia: float) -> float:
        '''
        Método para calcular o consumo do veículo
        Argumento: distancia (float): distância a ser percorrida
        '''
        self.distancia = distancia
        return distancia / self.__eficiencia