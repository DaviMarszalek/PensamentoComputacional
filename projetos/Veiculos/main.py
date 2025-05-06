from models.Veiculos import Veiculos

gol = Veiculos("Gol Copa", "Volkswagen", "IND-1010", "2006", "Amarelo", 0, 0, 0)

gol.mostrarInfos()  
gol.acelerar()
gol.mostrarInfos()
gol.frear()
gol.mostrarInfos()
gol.alterarPlaca("IND1A10")
print(gol.marca)
gol.mostrarInfos()
