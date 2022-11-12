saldo = 1000
saque = 200
limite = 100

operador_and = saldo >= saque and saque <= limite #false
print(operador_and)
operador_or = saldo >= saque or saque <= limite #true
print(operador_or)

operador_not = not 1000 > 1500 # true
print(operador_not)

lista_vazia = []
operador_not = not lista_vazia # True pois lista vazia tem valor booleano valor falso

string_com_valor = "string com valor"
operador_not = not string_com_valor # False pois string com valor tem valor booleano verdadeiro, logo a negacao dela é falso

string_sem_valor = ""
operador_not = not string_sem_valor # True pois string sem valor tem valor booleano falso, logo a negacao dela é verdadeira

# Precedencia 
# Parentese
# Esquerda para direita