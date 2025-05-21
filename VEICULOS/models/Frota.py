class Frota:
    def __init__(self, veiculos):
        
        self.__veiculos = [veiculos]
    
    def adicionar_veiculo(self, veiculo):
            self.__veiculos.append(veiculo)

    #def listar_veiculos(self):
       # return [veiculo.modelo for veiculo in self.__veiculos]

    '''
    def calcular_consumo_total(self, distancia):
        return sum(veiculo.calcular_consumo(distancia) for veiculo in self.__veiculos)
        consumo_total = frota.calcular_consumo_total(distancia)
    '''
    def consumo_total(self, distancia):
        consumo_total = 0
        for veiculo in self.__veiculos:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total    