class Filme:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.avaliacao = avaliacao

    def avaliar(self, nova_avaliacao):
        print(f"Avaliação do filme {self.titulo}: {self.avaliacao}")
        nova_avaliacao = float(input("Digite a nova nota de avaliação (0 a 10): "))
        if nova_avaliacao >= 0 and nova_avaliacao <= 10:
            self.avaliacao = nova_avaliacao
        else:
            print("Nota de avaliação inválida. Deve estar entre 0 e 10.")
     
    def exibir_informacoes(self):
        print("Título:", self.titulo)
        print("Gênero:", self.genero)
        print("Duração:", self.duracao, "minutos")
        print("Avaliação:", self.avaliacao)        
        
        
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
        
        