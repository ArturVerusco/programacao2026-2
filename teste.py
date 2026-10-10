nomes = list(input("Digite os nomes:"))

for i in range(len(nomes)):
    notas = input(f"Digite o preço do {nomes[i]}: ")

total = len(notas) / len(nomes)

print(total)
