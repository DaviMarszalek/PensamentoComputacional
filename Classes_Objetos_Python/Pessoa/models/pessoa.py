class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade 
        self.__altura = altura
        
    def aniversario(self,):
        self.__idade += 1
        print(f"Parabéns {self.__nome}, você agora tem {self.__idade} anos!")
       
    def crescer(self, nova_altura):
        nova_altura = float(input("Digite quanto cresceu em m: "))
        self.__altura += nova_altura
        print(f"{self.__nome} cresceu {nova_altura} m e agora tem {self.__altura} m de altura!")    
        
    def exibir_informacoes():
        print("Nome:", self.__nome)
        print("Idade:", self.__idade, "anos")
        print("Altura:", self.__altura, "m")  
        
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
                          