# Através ta identacao consegue determinar onde um bloco começa e termina (além da parte estética)
# 4 espaços em branco vale um tab rsrs
#Exemplo: 
def sacar(valor):
    saldo = 7900.50
    saldo -= valor
    print(f'valor foi sacado com sucesso, seu saldo novo é de : {saldo}')
sacar(900)