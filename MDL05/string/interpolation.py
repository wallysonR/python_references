# A formatação por % não é mais recomendada, mas vamos de Old Style pra livrar a conciencia:
nome = "Wally"
idade = 24
profissao = "desenvolvedor de Software"
linguagem = "Python e Java"

print("Olá, me chamo %s. eu tenho %d anos de idade, e trabalho como %s e tenho grande interesse nas linguagens %s." %(nome, idade, profissao, linguagem))

# Método Format
print("Olá, me chamo {}. eu tenho {} anos de idade, e trabalho como {} e tenho grande interesse nas linguagens {}.".format(nome, idade, profissao, linguagem)) # Esse método pode ser customizado passando a ordem das variaveis interpoladas
print("Olá, me chamo {3}. eu tenho {0} anos de idade, e trabalho como {1} e tenho grande interesse nas linguagens {2}.".format(idade, profissao, linguagem, nome))
print("Olá, me chamo {nome}. eu tenho {idade} anos de idade, e trabalho como {profissao} e tenho grande interesse nas linguagens {linguagem}.".format(idade=idade, profissao=profissao, linguagem=linguagem, nome=nome))# há essa opção de customização tbm

# f-string, muito parecido com o format, mas não precisamos colocar o .format nem o nome das variaveis. Pode passar a variável completa

print(f"Olá, me chamo {nome}. eu tenho {idade} anos de idade, e trabalho como {profissao} e tenho grande interesse nas linguagens {linguagem}.")

#Formatar strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")# o 2 representa o numero de casas
print(f"Valor de PI: {PI:10.2f}") # o 10 representa o numero de espacos