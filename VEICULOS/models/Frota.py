
class Frota:
    def __init__(self, veiculos):
        
        self.__veiculos = veiculos

    def adicionar_veiculo(self, veiculo):
            self.__veiculos.append(veiculo)

    def listar_veiculos(self):
        return [veiculo.modelo for veiculo in self.__veiculos]

    def calcular_consumo_total(self, distancia):
        return sum(veiculo.calcular_consumo(distancia) for veiculo in self.__veiculos)



  
    
    frota = Frota()
    frota.adicionar_veiculo(carro)
    frota.adicionar_veiculo(moto)
    frota.adicionar_veiculo(caminhao)

    
    print("Veículos na frota:", frota.listar_veiculos())

    
    consumo_total = frota.calcular_consumo_total(distancia)
    print(f"Consumo total da frota para {distancia} km: {consumo_total} litros")
    