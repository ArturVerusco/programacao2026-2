lista = []

for i in range(10):
    numeros = input(f"{i+1:2d} - Digite os números (ou FIM para sair): ")

    if numeros not numeros.isdecimal():
        print("Erro - numeros digitado não é um número.")
        continue

    num = int(numeros)

    if num not in lista:
        lista.append(num)

print("A lista digitada:" )
print(lista)