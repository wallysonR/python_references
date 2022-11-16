# Classe string no python tem é um pouco mais complexos,
# È bem rica com muita literatura para consumir.

# Metodos úteis :

# Maíscula, minúscula e título
curso = "pYtHon"
print(curso.upper()) # método upper converte todo mundo pra maiúsculo
print(curso.lower()) # método lower converte todo mundo pra minúsculo
print(curso.title()) # método title converte todo mundo pra minisculo, exceto a primeira letra

# Eliminando espaços em branco
print(curso.strip())# Elimina espaços em branco tanto da esqueda quanto da direita
print(curso.lstrip()) # Elimina espações em branco somente da esqueda
print(curso.rstrip())# Elimina espaços em branco somente da direita

#Junções e Centralização

curso = "Python"

print(curso.center(10,"#")) # Centraliza com o numero de caracteres que ele quer ocupar e qual o caracteres vc quer colocar, se não informar ele coloca espaço em branco
print(".".join(curso)) # O join funciona como iteravel, ele vai de item a item e coloca o que vc colocou como o "."