from models.livro import Livro

class TesteLivro:
    def testar_livro(self):
        meu_livro = Livro("Dom Quixote", "Miguel de Cervantes", 1605, 863)

        print("Informações iniciais do livro:")
        meu_livro.exibir_informacoes()
        print("-" * 20)

        print("Avançando uma página")
        meu_livro.avancar_pagina()

        meu_livro.exibir_informacoes()
        print("-" * 20)

        print("Voltando uma página")
        meu_livro.voltar_pagina()
        meu_livro.exibir_informacoes()
        print("-" * 20)

        print("Tentando avançar além do número de páginas")
        for _ in range(10):
            meu_livro.avancar_pagina()
        meu_livro.exibir_informacoes()
        print("-" * 20)

        print("Voltando para a primeira página")
        while meu_livro._Livro__pagina_atual > 1:  
            meu_livro.voltar_pagina()
        meu_livro.exibir_informacoes()
        print("-" * 20)

if __name__ == "__main__":
    teste = TesteLivro()
    teste.testar_livro()