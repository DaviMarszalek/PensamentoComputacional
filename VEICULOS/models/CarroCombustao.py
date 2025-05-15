from .Veiculos import Veiculos

class CarroCombustao(Veiculos):
    '''
    Classe que representa um carro a combustão
    '''
    def __init__(self, placa: str, modelo: str, marca: str,
                 ano: int, cor: str, valor_fipe: float,
                 combustivel: str, nPortas: int, nAssentos: int,
                 nCilindrada: int, nCambio: str, nivel_combustivel: int) -> None:
        
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        
        self.__combustivel = combustivel                
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindrada = nCilindrada
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel
        
    def __str__(self) -> str:
        '''
        Retorna uma string com as informações do carro a combustão
        '''
        #Reutiliza o método __str__ da classe pai(Veiculos)
        infos = Veiculos.__str__(self)
        #Adiciona as informações específicas do carro a combustão
        infos += f"Combustível: {self.__combustivel}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Cilindrada: {self.__nCilindrada}\n"
        infos += f"Câmbio: {self.__nCambio}\n" 
        infos += f"Nível de Combustível: {self.__nivel_combustivel}\n"  
        return infos 
    
    def abastecer(self, percentual_adicionado: int) -> bool:
        '''
        Método para abastecer o carro a combustão
        Argumentos:
            percentual (int): percentual adicionado
        Retorno:
           bool: True se foi possível abastecer, False se não
        '''
        
        novo_percentual = self.__nivel_combustivel + percentual_adicionado
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True
        return False