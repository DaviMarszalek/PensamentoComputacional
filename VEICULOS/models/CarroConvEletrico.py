from .CarroCombustao import CarroCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletrico( CarroCombustao, CarroEletrico):
    '''
    Classe que representa um carro a combustão convertido para elétrico
    '''
    def __init__(self, placa: str, modelo: str, marca: str,
                 ano: int, cor: str, valor_fipe: float,
                 combustivel: str, nPortas: int, nAssentos: int,
                 nCilindrada: int, nCambio: str, nivel_combustivel: int,
                 nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        
        CarroCombustao().__init__(placa, modelo, marca, ano, cor, valor_fipe,
                         combustivel, nPortas, nAssentos,
                         nCilindrada, nCambio, nivel_combustivel)
        
        CarroEletrico.__init__(placa, modelo, marca, ano, cor, valor_fipe, 
                               nAssentos, nPortas, nivel_bateria, tipo_bateria, autonomia)
        
    def __str__(self) -> str:
        infos = CarroCombustao().__str__(self)
        infos += f"Nível de Bateria: {CarroEletrico.get_nivel_bateria(self)}\n"
        infos += f"Tipo de Bateria: {CarroEletrico.get_tipo_bateria(self)}\n"    
        infos += f"Autonomia: {CarroEletrico.get_autonomia(self)}\n"
        return infos    
    
    def abastecer(self, percentual_adicionado: float) -> bool:
        '''
        Desativa o método abastecer em carro convertido elétrico
        Argumentos:
            percentual (int): percentual adicionado
        Retorno:
            False, pos não pode abastecer com combustível
        '''
        print(f"Carro convertido para elétrico, não é possível abastecer com combustível\n")
        return False
    
    