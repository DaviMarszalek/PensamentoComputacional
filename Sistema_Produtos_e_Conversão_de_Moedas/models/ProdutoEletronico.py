from .Produtos import Produto

class ProdutoEletronico(Produto):
  def __init__(self, nome: str, preco: float, moeda: str, voltagem: str):
    super().__init__(nome, preco, moeda)
    self.__voltagem = voltagem

  def __str__(self) -> str:
    infos = super().__str__()
    infos += f"Voltagem: {self.__voltagem}\n"
    infos += f"Eletrônico"
    return infos