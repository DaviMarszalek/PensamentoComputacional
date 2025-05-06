class Filme:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.__titulo = titulo
        self.__genero = genero
        self.__duracao = duracao
        self.__avaliacao = avaliacao

    def avaliar(self, nova_avaliacao):
        print(f"Avaliação do filme {self.__titulo}: {self.__avaliacao}")
        nova_avaliacao = float(input("Digite a nova nota de avaliação (0 a 10): "))
        if nova_avaliacao >= 0 and nova_avaliacao <= 10:
            self.__avaliacao = nova_avaliacao
        else:
            print("Nota de avaliação inválida. Deve estar entre 0 e 10.")
     
    def exibir_informacoes(self):
        print("Título:", self.__titulo)
        print("Gênero:", self.__genero)
        print("Duração:", self.__duracao, "minutos")
        print("Avaliação:", self.__avaliacao)        
        
        
class TesteFilme:
    def testar_filme(self):
        filme = Filme("O Senhor dos Anéis", "Fantasia", 178, 9.0)
        
        print("Informações iniciais do filme:")
        filme.exibir_informacoes()
        print("-" * 20)
        
        print("Nova avaliação do filme")
        filme.avaliar(10.00)
        
        filme.exibir_informacoes()
        print("-" * 20)        
        
        