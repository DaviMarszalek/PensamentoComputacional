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
    
    def setPlaca(self, placa: str) -> None:
        '''
        Altera a placa do veículo
        
        Argumento: placa (str): nova placa do veículo
        Saída: True se OK
        '''
        
        placa_validada = self.__validar_placa(placa)
        if placa_validada:
            self.__placa = placa_validada
            return True
        return False
    
    def __validar_placa(self, placa: str) -> str | None:
        '''
        Valida se a placa segue o padrão brasileiro (3 letras e 4 números).
        Retorna a placa formatada se válida, None caso contrário.
        '''
        placa = placa.upper()
        if len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric():
            return placa
        else:
            print("Erro: Placa inválida. O formato deve ser 3 letras seguidas de 4 números (ex: ABC1234).")
            return None
    
    def setValorFipe(self, valor: float) -> None:
        '''
        Altera o valor de fipe do veículo
        
        Argumento: valor (float): novo valor da fipe do veículo
        Saída: True se OK
        '''
        self.__valor_fipe = valor
        return True
    
    def calcular_consumo(self, distancia: float) -> float:
        '''
        Método para calcular o consumo do veículo
        Argumento: distancia (float): distância a ser percorrida
        '''
        self.distancia = distancia
        return distancia / self.__eficiencia
    
    def __eq__(self, other: object) -> bool:
        '''
        Método para comparar dois veículos
        Argumento: outro veículo
        Saída: True se os veículos forem iguais, False caso contrário
        '''
        if isinstance(other, Veiculos):
            return self.__placa == other.__placa
        return False
         
         
         