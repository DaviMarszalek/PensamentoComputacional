def imprime_filmes(filmes):
    for filme in filmes:
        print(f"Nome: {filme['nome']} - Nota: {filme['nota']}")

def duplicidade(novo, filmes):
    for filme in filmes:
        if novo.lower() == filme['nome'].lower():
            return True
    return False

contador = 0
filmes = []
notas = []

# Mensagem de opções
op_string = "Para editar digite:"
op_string += "\nADD para adicionar um filme,"
op_string += "\nRMV para remover um filme,"
op_string += "\nEDT para editar um filme,"
op_string += "\nE para encerrar a listagem."
print(op_string)

while True:
    opcao = input("\nDigite uma opção (ADD/RMV/EDT/E): ").upper()

    if opcao == 'ADD':
        nome_filme = input('Informe o nome do filme: ')

        if duplicidade(nome_filme, filmes):
            print("Este filme já foi cadastrado. Tente outro.")
            continue

        while True:
            try:
                nota_str = input('Informe a nota do filme entre 0.0 e 10.0: ').replace(',', '.')
                nota = float(nota_str)
                if 0.0 <= nota <= 10.0:
                    break
                else:
                    print("Nota inválida. Deve estar entre 0.0 e 10.0.")
            except ValueError:
                print("Digite um valor numérico válido.")

        filmes.append({"nome": nome_filme, "nota": nota})
        notas.append(nota)
        contador += 1

        if contador >= 1000:
            print("Limite de 1000 filmes atingido.")
            break

    elif opcao == 'RMV':
        nome_filme = input("Digite o nome do filme a remover: ")
        for filme in filmes:
            if filme["nome"].lower() == nome_filme.lower():
                notas.remove(filme["nota"])
                filmes.remove(filme)
                contador -= 1
                print("Filme removido com sucesso.")
                break
        else:
            print("Filme não encontrado.")

    elif opcao == 'EDT':
        nome_filme = input("Digite o nome do filme que quer editar: ")
        for filme in filmes:
            if filme["nome"].lower() == nome_filme.lower():
                novo_nome = input("Novo nome do filme (pressione Enter para manter o atual): ")
                if novo_nome and not duplicidade(novo_nome, filmes):
                    filme["nome"] = novo_nome
                elif novo_nome:
                    print("Esse novo nome já está em uso. Nome não alterado.")

                while True:
                    nova_nota = input("Nova nota do filme (pressione Enter para manter a atual): ")
                    if nova_nota == '':
                        break
                    try:
                        nova_nota_float = float(nova_nota.replace(',', '.'))
                        if 0.0 <= nova_nota_float <= 10.0:
                            notas.remove(filme["nota"])
                            filme["nota"] = nova_nota_float
                            notas.append(nova_nota_float)
                            break
                        else:
                            print("Nota inválida. Deve estar entre 0.0 e 10.0.")
                    except ValueError:
                        print("Digite um valor numérico válido.")
                print("Filme atualizado com sucesso.")
                break
        else:
            print("Filme não encontrado.")

    elif opcao == 'E':
        break

    else:
        print("Opção inválida. Tente novamente.")

if filmes:
    print("\n--- FILMES CADASTRADOS ---")
    imprime_filmes(filmes)
    print("\nA média das notas é:", round(sum(notas) / contador, 2))
    print("Total de filmes cadastrados:", contador)
else:
    print("Nenhum filme foi cadastrado.")
