from .Produtos import Produto

class ProdutoAlimenticio(Produto):
  def __init__(self, nome: str, preco: float, moeda: str, validade: str):
    super().__init__(nome, preco, moeda)
    self.__validade = validade

  def __str__(self) -> str:
    infos = super().__str__()
    infos += f"Validade: {self.__validade}\n"
    infos += f"Alientício"
    return infos