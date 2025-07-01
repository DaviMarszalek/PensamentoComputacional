from models import Veiculo

class Proprietario():
    def __init__(self, nome, cpf, placa_veiculo=None):
        self.nome = nome
        self.cpf = cpf
        self.placa_veiculo = placa_veiculo # Placa do veículo que possui
        
       

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_placa_veiculo(self):
        return self.placa_veiculo


    def __str__(self):
        info = f"Nome: {self.nome}, CPF: {self.cpf}, Placa: {self.placa_veiculo}"
        return info
       