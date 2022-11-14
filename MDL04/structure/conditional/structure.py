# permite o desvio de fluxos de controle, quando determiminadas expressões lógicas são atendidas

saldo = 2000.0
saque = float(input("Infome o valor que quer sacar:"))

if saldo>saque:
    saldo -= saque
    print(f'saque efetuado com sucesso... Seu novo saldo é de: {saldo}')
elif saldo == saque:
    print("Esse saque é possível porem você ficará sem saldo na sua conta...")
    deseja_continuar = input("Deseja continuar ?")
    if deseja_continuar == "sim" or deseja_continuar == "Sim":
        saldo-= saque
        print(f'Saque realizado... Seu saldo é de {saldo}')
    elif deseja_continuar == "não" or deseja_continuar == "Não":
        print('Okay. Até mais...')
    else: 
        print("Operacao invalida");
else:
    print("Sinto muito mas seu saldo é insulficiente")