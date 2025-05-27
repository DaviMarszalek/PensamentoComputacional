class Produto:
  def __init__(self, nome: str, preco: float, moeda: str):
    self.__nome = nome
    self.__preco = preco
    self.__moeda = moeda

  def get_nome(self):
    return self.__nome

  def set_nome(self, nome: str):
    self.__nome = nome

  def get_preco(self):
    return self.__preco

  def set_preco(self):
    self.__preco = preco

  def get_moeda(self):
    return self.__moeda

  def set_moeda(self, moeda: str):
    self.__moeda = moeda


  def __str__(self) -> str:
    infos = f"Nome: {self.nome}\n"
    infos += f"Preço: {self.preco}\n"
    infos += f"Moeda: {self.moeda}\n"
    return infos

