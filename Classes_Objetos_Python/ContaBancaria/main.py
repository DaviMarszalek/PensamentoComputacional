from models.contabancaria import ContaBancaria

banco = []

def encontrar_conta(titular):
    for conta in banco:
        if conta.titular.lower() == titular.lower():
            return conta
    return None

def excluir_conta():
    print("\n--- Excluir Conta ---")
    titular_excluir = input("Digite o titular da conta para excluir: ")
    conta_excluir = encontrar_conta(titular_excluir)
    if conta_excluir:
        if conta_excluir.saldo != 0:
            print(f"A conta de {conta_excluir.titular} tem saldo de R${conta_excluir.saldo:.2f}.")
            print("Para excluir, o saldo precisa ser zero.")
            # Simplificando a lógica de exclusão para iniciantes
        else:
            banco.remove(conta_excluir)
            print(f"Conta de {conta_excluir.titular} excluída.")
    else:
        print(f"Conta com titular '{titular_excluir}' não encontrada.")

while True:
    print("\n--- Sistema Bancário ---")
    print("1 - Criar conta")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Transferir")
    print("5 - Exibir saldo")
    print("6 - Exibir histórico")
    print("7 - Excluir conta")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            print("\n--- Criar Conta ---")
            titular = input("Digite o nome do titular: ")
            while True:
                try:
                    saldo = float(input("Digite o saldo inicial: "))
                    break
                except ValueError:
                    print("Por favor, digite um número válido para o saldo.")
            limite = 200
            if saldo > 0:
                limite += int(saldo / 2)
            while True:
                o = input("Deseja cadastrar chaves PIX? (s/n): ")
                if o == 's':
                    try:   
                        chave_pix_celular = int(input("Digite a chave pix CELULAR: "))
                        chave_pix_email = str(input("Digite a chave pix EMAIL: "))    
                        chave_pix_CPF = int(input("Digite a chave pix CPF: "))
                    except ValueError:
                        print("Por favor, digite um valor válido.")     
            conta = ContaBancaria(titular, saldo, limite, [chaves_pix_celular, chaves_pix_email, chave_pix_CPF] [])
            banco.append(conta)
            print(f"Conta criada para {titular}.")        
        elif opcao == 2:
            print("\n--- Sacar ---")
            if banco:
                titular = input("Digite o nome completo do titular da conta: ")
                conta = encontrar_conta(titular)
                if conta:
                    valor = input("Digite o valor para sacar: ")
                    if valor:
                        valor = float(valor)
                        conta.sacar(valor)
                else:
                    print("Conta não encontrada.")
            else:
                print("Não há contas cadastradas.")
        elif opcao == 3:
            print("\n--- Depositar ---")
            if banco:
                titular = input("Digite o nome completo do titular da conta: ")
                conta = encontrar_conta(titular)
                if conta:
                    valor = input("Digite o valor para depositar: ")
                    if valor:
                        valor = float(valor)
                        conta.depositar(valor)
                else:
                    print("Conta não encontrada.")
            else:
                print("Não há contas cadastradas.")
        elif opcao == 4:
            print("\n--- Transferir ---")
            if len(banco) >= 2:
                titular_origem = input("Digite o nome completo do titular da conta de origem: ")
                conta_origem = encontrar_conta(titular_origem)
                if conta_origem:
                    titular_destino = input("Digite o nome completo do titular da conta de destino: ")
                    conta_destino = encontrar_conta(titular_destino)
                    if conta_destino:
                        valor = input("Digite o valor para transferir: ")
                        if valor:
                            valor = float(valor)
                            conta_origem.transferir(valor, conta_destino)
                    else:
                        print("Conta de destino não encontrada.")
                else:
                    print("Conta de origem não encontrada.")
            else:
                print("É necessário ter pelo menos duas contas para transferir.")
        elif opcao == 5:
            print("\n--- Exibir Saldo ---")
            if banco:
                titular = input("Digite o nome completo do titular da conta: ")
                conta = encontrar_conta(titular)
                if conta:
                    conta.exibir_saldo()
                else:
                    print("Conta não encontrada.")
            else:
                print("Não há contas cadastradas.")
        elif opcao == 6:
            print("\n--- Exibir Histórico ---")
            if banco:
                titular = input("Digite o nome completo do titular da conta: ")
                conta = encontrar_conta(titular)
                if conta:
                    conta.exibir_historico()
                else:
                    print("Conta não encontrada.")
            else:
                print("Não há contas cadastradas.")
        elif opcao == 7:
            excluir_conta()
        elif opcao == 0:
            print("Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida.")
    else:
        print("Digite um número.")