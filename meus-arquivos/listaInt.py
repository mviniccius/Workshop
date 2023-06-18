from random import randint
soma = 0
maior = 0
menor = 99999999
numeros = []
impares = []
pares = []
tamanho = 10

for i in range(0, tamanho):
    numeros.append(randint(0, 1000))
print(numeros)
for i in range(0, tamanho):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
    soma += numeros[i]
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
print(f"O maior numero:{maior}")
print(f"O menor numero:{menor}")
print(f"A soma dos numeros:{soma}")
print(f"Numeros pares:{pares}")
print(f"Numeros Impares:{impares}")


                