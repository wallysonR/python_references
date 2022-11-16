# fatiamendo de string é uma técnica utilizada para retornar sibstrings (partes de um string origirinal), informando o inicio (start), fim (stop) e passos(step)
# [start:stop[,steps]]

nome = "Wallyson Roberto Leite dos santos"
print(nome[0]);
print(nome[:8]) # Se não for informado o start ele considera o start como o começo da string
print(nome[9:]) # Se não for informado o end ele vai considerar o stop como o final da string
print(nome[9:16])# Start e Stop definidos
print(nome[9:16:2])# Start, Stop e Step definidos
print(nome[:]) # Não passa nada retorna tudo
print(nome[::-1]) # Passando Step como -1 vc consegue fazer o espelhamento, ou seja ao contrario
print(nome[-1]) # funciona com numeros negativos tbm, ou seja nesse caso ta pegando a ultima letra