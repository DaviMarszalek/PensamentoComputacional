from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen",
                  2018, "Vermelho", 47793)

jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Volkswagen",
                            2025, "Vermelho", 250000, "Gasolina",
                            4, 5, 2000, "AT 7", 24)

tesla_model_s = CarroEletrico("JDN0A00", "Tesla Model S", "Tesla",
                              2021, "Branco", 950000, 5, 4,
                              65, "Lithium-ion", 491)

fusca_eletrico = CarroConvEletrico(placa="IAA0D36",         modelo="Fusca 1600 Elétrico", 
                                   marca="Volkswagen",      ano=1975,               
                                   cor="Azul",              valor_fipe=70000, 
                                   combustivel="Gasolina",  nPortas=4, 
                                   nAssentos=5,             nCilindrada=1600, 
                                   nCambio="MT 4",          nivel_combustivel=24, 
                                   nivel_bateria=65,        tipo_bateria="Lithium-ion",
                                   autonomia=151)

xj6 = Moto("JDN0A00", "XJ6", "Jaguar",
                  2021, "Preto", 950000, 20)

astra = Carro("JDN0A11", "Astra", "Chevrolet",
                  2021, "Preto", 950000, 12)

scania = Caminhao("JDN0A22", "Scania 30 G", "Scania",
                  2021, "Preto", 2500000, 5)



distancia = int(input("Informe a distância do percurso e descubra qual a eficiencia do veículo:\n"))
print("Consumo do Astra: ", astra.calcular_consumo(distancia), "L")
print("Consumo da XJ6: ", xj6.calcular_consumo(distancia), "L")
print("Consumo da Scania: ", scania.calcular_consumo(distancia), "L")




