nomes = list(input("Digite os nomes: ").split())

for i in range(len(nomes)):
    notas = input(f"Digite essa quantidade de notas {nomes[i]}: ")

total = len(notas) / len(nomes)

print(total)
