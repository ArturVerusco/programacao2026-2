lista = []

for i in range(10):
    numeros = input("Digite os números (ou FIM para sair): ")
    if numeros not in num:
            num.append(numeros)

    if numeros.isdecimal():
        print("Erro - numeros digitado não é um número.")
        continue

    num = int(numeros)

    if num not in lista:
        lista.append(num)

print("A lista digitada:" )
print(lista)