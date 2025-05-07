class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade 
        self.altura = altura
        
    def aniversario(self,):
        self.idade += 1
        print(f"Parabéns {self.nome}, você agora tem {self.idade} anos!")
       
    def crescer(self, nova_altura):
        nova_altura = float(input("Digite quanto cresceu em m: "))
        self.altura += nova_altura
        print(f"{self.nome} cresceu {nova_altura} m e agora tem {self.altura} m de altura!")    
        
    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade, "anos")
        print("Altura:", self.altura, "m")  
        
class TestePessoa:
    def testar_pessoa(self):
        pessoa = Pessoa("João", 19, 1.71)
        
        print("Informações:")
        pessoa.exibir_informacoes()
        print("-" * 20)                  
        
        print("Aniversário")
        pessoa.aniversario()
        print("-" * 20)
        
        print("Crescimento")
        pessoa.crescer(12)
        print("-" * 20)        
                          
        print("Informações:")
        pessoa.exibir_informacoes()
        print("-" * 20)                  