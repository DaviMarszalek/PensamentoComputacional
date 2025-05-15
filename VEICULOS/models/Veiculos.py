class Veiculos:
    
    '''
    Classe com as principais funcionalidades do sistema de veiculs
    '''
    
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        '''
        Construtor da classe Veiculos
        '''
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe
        
    def __str__(self) -> str:
        '''
      Retorna uma string com as informações do veículo
        '''
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
        return infos
           
    def getPlaca(self) -> str:
        '''
       retorna a placa do veículo
        '''
        return self.__placa
    
    def setValorFipe(self, valor: float) -> None:
        '''
        Altera o valor de fipe do veículo
        
        Argumento: valor (float): novo valor da fipe do veículo
        Saída: True se OK
        '''
        self.__valor_fipe = valor
        return True
    
    