from .Veiculos import Veiculos

class VeiculoEletrico(Veiculos):
    '''
    Classe que representa um veículo elétrico
    '''

    def __init__(self, placa: str, modelo: str, marca: str,
                 ano: int, cor: str, valor_fipe: float,
                 nPortas: int, nAssentos: int, nivel_bateria: int,
                 tipo_bateria: str, autonomia: int, eficiencia: float) -> None:
        '''
        Construtor da classe VeiculoEletrico
        '''
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)

        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
        self.__eficiencia = eficiencia # Defini a eficiência aqui

    def __str__(self) -> str:
        '''
        Retorna uma string com as informações do veículo elétrico
        '''
        infos = super().__str__()
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        infos += f"Nível de bateria: {self.__nivel_bateria}%\n" # Adicionei o símbolo de porcentagem
        infos += f"Tipo de bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia} km\n"
        infos += f"Eficiencia: {self.__eficiencia} kWh/km\n" # Especificando a unidade
        return infos

    def recarregar(self, percentual_adicionado: int) -> bool:
        '''
        Método para recarregar o Veiculo Eletrico
        Argumentos:
            percentual (int): percentual adicionado
        Retorno:
            bool: True se foi possível recarregar, False se não
        '''

        novo_percentual = self.__nivel_bateria + percentual_adicionado
        if novo_percentual <= 100:
            self.__nivel_bateria = novo_percentual
            return True
        return False

    def calcular_consumo(self, distancia: float) -> float:
        """
        Calcula o consumo de energia para a distância especificada.
        Para veículos elétricos, o consumo é dado em kWh.
        """
        return distancia * self.__eficiencia