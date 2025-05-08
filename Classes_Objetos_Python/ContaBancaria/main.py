from models.contabancaria import ContaBancaria

'''
- 1 Criar conta
- 2 Sacar
- 3 Depositar
- 4 Transferir
- 5 Exibir saldo
- 6 Exibir histórico
- 7 Excluir conta
'''

banco = []

a = int(input(f"Bem-vindo ao sistema de contas bancárias!\n \n1 - Criar conta\n2 - Sacar\n3 - Depositar\n4 - Transferir\n5 - Exibir saldo\n6 - Exibir histórico\n7 - Excluir conta \nEscolha uma opção: "))
if a == 1:
    titular = str(input("Digite o nome completo do titular da conta:"))
    saldo = float(input("Digite o saldo inicial da conta: "))
    limite = 200
    if saldo > 0:
        limite = limite + int(saldo / 2)
    banco.append(ContaBancaria(titular, saldo, limite, [])) 
    for conta in banco:
        if conta.titular == titular:
            print(f"{titular} tem R${conta.saldo} em conta e possui um limite de R${conta.limite}!") 
if a == 2:
    titular_saque = input("Digite o titular da conta que deseja sacar: ")
    saque = float(input("Informe o valor do saque: "))
    for conta in banco:
        if conta.titular == titular_saque:
            conta.sacar(saque)
        else:
            print(f"Conta com titular '{titular_saque}' não encontrada.")               
    

'''
titular = input("Digite o titular da conta que deseja ver o saldo:")

for conta in banco:
    if conta.titular == titular:
        print(f"O {titular} tem R${conta.saldo} em conta!")    
'''    