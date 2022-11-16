N = int(input())
lista = []
for numeros in range(0,N):
  A,B = input().split(" ")
  A = A[-len(B):]
  if B in A:
    lista.append("encaixa")
  else:
    lista.append("nao encaixa")

for item in lista:
    print(item)  