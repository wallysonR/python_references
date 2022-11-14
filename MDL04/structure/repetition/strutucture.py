#repete um comando com numero de repeticoes predefinidos ou não

# For - faz sentido usar um for quando quisermos saber o numero de iteração ou quando queremos percorrer um objeto iteravel;

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() #quebra a linha      

# Ranger - Delimita um intervalo de valores é 
# uma função Built-nt
# inicio é inclusivo e fim é exclusico
# ranger(stop) -. ranger object
# ranger(start, stop[, step]) -> ranger object
range(4)
list(range(4))

for numero in range(0,11):
    if(numero == 10):
        print(numero)    
    else:
        print(numero, end=" ")

#outro exemplo com steps
for numero in range(0, 51, 5):
    print(numero, end=" ")

#While: itera até que uma condicao seja atendida,
#  faz sentido ser usado quando não sabemos quantas vezes precisaremos executar.
opcao = -1
while opcao != 0:
    opcao = int(input("[1] sacar \n [2] Extrato \n [0] sair \n:"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato ...")