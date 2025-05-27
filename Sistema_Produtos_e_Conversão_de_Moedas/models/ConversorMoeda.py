from .Produtos import Produto

class MoedaInvalidaError(Exception):
    pass

class ConversorMoeda(Produto):
    def __init__(self):
        self._cotacao_usd_para_brl = 5.05
        self._cotacao_eur_para_brl = 6.14
        self._cotacao_eur_para_usd = 1.22

    def converter_preco_para_usd(self, produto: Produto ) -> float:
     
        try:    
            if Produto.get_moeda() == "BRL":
                Produto.set_preco(Produto.get_preco() / self._cotacao_usd_para_brl)
                Produto.set_moeda("USD")
                return True
            elif Produto.get_moeda() == "EUR":
                Produto.set_preco(Produto.get_preco() * self._cotacao_eur_para_usd)
                Produto.set_moeda("USD")
                return True
            else: 
                Produto.get_moeda() == "USD"
                return False
        except MoedaInvalidaError:
            f"Moeda '{Produto.get_moeda()}' não suportada para a conversão para USD."
            
        
    def converter_preco_para_brl(self, produto: Produto) -> float:
        if Produto.get_moeda() == "USD":
            Produto.set_preco(Produto.get_preco() * self._cotacao_usd_para_brl)
            Produto.set_moeda("BRL")
            return True
        elif Produto.get_moeda() == "EUR":
            Produto.set_preco(Produto.get_preco() * self._cotacao_eur_para_brl)
            Produto.set_moeda("BRL")
            return True
        elif Produto.get_moeda() == "BRL":
            return False
        else:
            raise MoedaInvalidaError("Moeda", Produto.get_moeda(), "não suportada para a conversão para BRL.")
        
    def converter_preco_para_eur(self, produto: Produto) -> bool:
        if Produto.get_moeda() == "BRL":
            Produto.set_preco(Produto.get_preco() / self._cotacao_eur_para_brl)
            Produto.set_moeda("EUR")
            return True
        elif Produto.get_moeda() == "USD":
            Produto.set_preco(Produto.get_preco() / self._cotacao_eur_para_usd)
            Produto.set_moeda("EUR")
            return True
        elif Produto.get_moeda() == "EUR":
            return False
        else:
            raise MoedaInvalidaError(f"Moeda '{Produto.get_moeda()}' não suportada para a conversão para EUR.")  
            