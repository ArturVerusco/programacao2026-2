nomes = list(input("Digite os nomes:"))
notas = 0

if notas != 1:
    notas = input("Digite essa quantidade de notas:",len(nomes))

total = len(notas) / len(nomes)

print(total)