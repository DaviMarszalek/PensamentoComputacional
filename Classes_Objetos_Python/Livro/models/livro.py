# models/livro.py - Classes e estruturas de dados
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__numero_paginas = numero_paginas
        self.__pagina_atual = 1  # Inicializa a página atual como 1

    def avancar_pagina(self):
        if self.__pagina_atual < self.__numero_paginas:
            self.__pagina_atual += 1

    def voltar_pagina(self):
        if self.__pagina_atual > 1:
            self.__pagina_atual -= 1

    def exibir_informacoes(self):
        print("Título:", self.__titulo)
        print("Autor:", self.__autor)
        print("Ano de Publicação:", self.__ano_publicacao)
        print("Número de Páginas:", self.__numero_paginas)
        print("Página Atual:", self.__pagina_atual)