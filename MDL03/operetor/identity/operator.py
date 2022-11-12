# usado para comparar se os objetos ocupam a mesma regiao de memoria
curso = "Curso de python"
nome_curso = curso

operador_is = curso is nome_curso # True pois ele também tem o mesmo valor
print(operador_is)

operador_is_not = curso is not nome_curso # False por é a negacao do operador is
print(operador_is_not)

saldo, limite = 200, 200

operador_is = saldo is limite #true pois ambos possuem o mesmo valor
print(operador_is)
