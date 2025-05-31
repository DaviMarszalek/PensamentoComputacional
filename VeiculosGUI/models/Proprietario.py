import re # Importa o módulo de expressões regulares
import tkinter as tk
from tkinter import messagebox # Para exibir mensagens

class Proprietario:
    def __init__(self, nome: str, CPF: str, placa: str, veiculo_desc: str): # Alterado 'veiculo' para 'veiculo_desc' para evitar confusão com um potencial objeto Veiculo
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        self.__nome = nome

        if not self.validar_cpf(CPF):
            raise ValueError("CPF inválido.")
        self.__cpf = self._limpar_cpf(CPF) # Armazena o CPF limpo

        if not self.validar_placa(placa):
            raise ValueError("Placa inválida.")
        self.__placa = placa.upper() # Armazena a placa em maiúsculas

        if not veiculo_desc:
            raise ValueError("Descrição do veículo não pode ser vazia.")
        self.__veiculo_desc = veiculo_desc # Descrição do veículo (ex: "Carro Gol 1.0")

    @staticmethod
    def _limpar_cpf(cpf: str) -> str:
        """Remove caracteres não numéricos do CPF."""
        return "".join(filter(str.isdigit, cpf))

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Valida o CPF utilizando o algoritmo padrão."""
        cpf_limpo = Proprietario._limpar_cpf(cpf)

        if len(cpf_limpo) != 11 or len(set(cpf_limpo)) == 1: # Verifica se tem 11 dígitos e se não são todos iguais
            return False

        # Calcula o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf_limpo[i]) * (10 - i)
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        if digito1 != int(cpf_limpo[9]):
            return False

        # Calcula o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf_limpo[i]) * (11 - i)
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        return digito2 == int(cpf_limpo[10])

    @staticmethod
    def validar_placa(placa: str) -> bool:
        """Valida a placa (formatos antigo e Mercosul)."""
        if not placa:
            return False
        placa_upper = placa.upper()
        # Padrão antigo: LLLNNNN (ex: ABC1234)
        padrao_antigo = re.compile(r"^[A-Z]{3}\d{4}$")
        # Padrão Mercosul: LLLNLNN (ex: ABC1D23)
        padrao_mercosul = re.compile(r"^[A-Z]{3}\d[A-Z]\d{2}$")

        return bool(padrao_antigo.match(placa_upper) or padrao_mercosul.match(placa_upper))

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        self.__nome = nome

    @property
    def cpf(self) -> str:
        # Retorna o CPF formatado para exibição
        return f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}"


    @cpf.setter
    def cpf(self, cpf_novo: str):
        if not self.validar_cpf(cpf_novo):
            raise ValueError("CPF inválido.")
        self.__cpf = self._limpar_cpf(cpf_novo)


    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, placa_nova: str):
        if not self.validar_placa(placa_nova):
            raise ValueError("Placa inválida.")
        self.__placa = placa_nova.upper()

    @property
    def veiculo_desc(self) -> str:
        return self.__veiculo_desc

    @veiculo_desc.setter
    def veiculo_desc(self, veiculo_desc_novo: str):
        if not veiculo_desc_novo:
            raise ValueError("Descrição do veículo não pode ser vazia.")
        self.__veiculo_desc = veiculo_desc_novo
        
    # "adicionar veículo" é interpretado como atualizar as informações do veículo atual.
    # Se um Proprietario pudesse ter múltiplos veículos, o design da classe seria diferente
    # (ex: uma lista de objetos Veiculo ou pares de placa/veiculo_desc)
    def atualizar_veiculo_info(self, nova_placa: str, nova_veiculo_desc: str):
        """Atualiza as informações do veículo associado ao proprietário."""
        if not self.validar_placa(nova_placa):
            raise ValueError("Nova placa inválida.")
        if not nova_veiculo_desc:
            raise ValueError("Nova descrição do veículo não pode ser vazia.")
        self.__placa = nova_placa.upper()
        self.__veiculo_desc = nova_veiculo_desc
        print(f"Veículo atualizado para: Placa {self.__placa}, Descrição {self.__veiculo_desc}")


    def __str__(self) -> str:
        # O CPF já é formatado pelo getter, então usamos self.cpf diretamente
        infos = f"Nome: {self.__nome}\n"
        infos += f"CPF: {self.cpf}\n" # Usa o getter que formata
        infos += f"Placa: {self.__placa}\n"
        infos += f"Veículo: {self.__veiculo_desc}"
        return infos